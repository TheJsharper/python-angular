import {
  AfterViewChecked,
  AfterViewInit,
  Component,
  ElementRef,
  HostListener,
  OnDestroy,
  ViewChild,
} from '@angular/core';
import { MatPaginatorModule, MatPaginator } from '@angular/material/paginator';
import { MatTableModule, MatTableDataSource } from '@angular/material/table';
import { ELEMENT_DATA, PeriodicElement } from '../element-data';

@Component({
  selector: 'app-elements-table',
  standalone: true,
  imports: [MatTableModule, MatPaginatorModule],
  templateUrl: './elements-table.html',
  styleUrls: ['./elements-table.scss'],
})
export class ElementsTableComponent implements AfterViewInit, AfterViewChecked, OnDestroy {
  displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];
  dataSource = new MatTableDataSource<PeriodicElement>(ELEMENT_DATA);
  pageSizeOptions: number[] = [10];
  currentPageSize = 10;
  private readonly minPageSize = 1;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild('tableScroll') tableScrollRef!: ElementRef<HTMLDivElement>;
  private resizeObserver?: ResizeObserver;
  private resizeRafId?: number;
  private lastLayoutSignature = '';

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
    this.schedulePageSizeRecalc();

    this.resizeObserver = new ResizeObserver(() => {
      this.schedulePageSizeRecalc();
    });
    this.resizeObserver.observe(this.tableScrollRef.nativeElement);
  }

  ngAfterViewChecked(): void {
    this.updatePageSizeFromViewport();
  }

  @HostListener('window:resize')
  onWindowResize(): void {
    this.schedulePageSizeRecalc();
  }

  ngOnDestroy(): void {
    if (this.resizeRafId !== undefined) {
      cancelAnimationFrame(this.resizeRafId);
    }
    this.resizeObserver?.disconnect();
  }

  private schedulePageSizeRecalc(): void {
    if (this.resizeRafId !== undefined) {
      cancelAnimationFrame(this.resizeRafId);
    }
    this.resizeRafId = requestAnimationFrame(() => {
      this.updatePageSizeFromViewport();
    });
  }

  private updatePageSizeFromViewport(): void {
    const scrollEl = this.tableScrollRef?.nativeElement;
    if (!scrollEl || !this.paginator) return;

    const headerRow = scrollEl.querySelector('.mat-mdc-header-row') as HTMLElement | null;
    const bodyRow = scrollEl.querySelector('.mat-mdc-row') as HTMLElement | null;
    const headerHeight = headerRow?.offsetHeight ?? 56;
    const rowHeight = bodyRow?.offsetHeight ?? 52;
    const layoutSignature = `${scrollEl.clientHeight}:${headerHeight}:${rowHeight}`;
    if (layoutSignature === this.lastLayoutSignature && this.paginator.pageSize === this.currentPageSize) return;

    this.lastLayoutSignature = layoutSignature;
    const availableBodyHeight = Math.max(0, scrollEl.clientHeight - headerHeight);
    const nextPageSize = Math.max(this.minPageSize, Math.floor(availableBodyHeight / rowHeight));

    if (this.currentPageSize === nextPageSize) return;

    this.currentPageSize = nextPageSize;
    const previousPageIndex = this.paginator.pageIndex;
    this.paginator.pageSize = nextPageSize;
    this.pageSizeOptions = [nextPageSize];

    const maxPageIndex = Math.max(0, Math.ceil(this.dataSource.data.length / nextPageSize) - 1);
    if (this.paginator.pageIndex > maxPageIndex) {
      this.paginator.pageIndex = maxPageIndex;
    }

    this.paginator.page.next({
      pageIndex: this.paginator.pageIndex,
      previousPageIndex,
      pageSize: this.paginator.pageSize,
      length: this.paginator.length,
    });
  }
}
