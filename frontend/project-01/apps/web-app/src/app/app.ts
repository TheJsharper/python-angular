
import { AfterViewInit, Component, ElementRef, NgZone, OnDestroy, ViewChild, signal, inject } from '@angular/core';
import { RouterModule } from '@angular/router';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatTooltipModule } from '@angular/material/tooltip';

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const THEMES = ['va-corporate', 'va-steel'] as const;
type Theme = typeof THEMES[number];

@Component({
  imports: [
    RouterModule,
    MatSidenavModule,
    MatToolbarModule,
    MatListModule,
    MatIconModule,
    MatButtonModule,
    MatTooltipModule,
  ],
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class App implements AfterViewInit, OnDestroy {
  private ngZone = inject(NgZone);

  @ViewChild('footTab') private footTabRef!: ElementRef<HTMLElement>;

  protected title = 'VA App';
  protected theme = signal<Theme>('va-corporate');

  private dragging = false;
  private startX = 0;
  private scrollLeft = 0;
  private movedPx = 0;
  private readonly DRAG_THRESHOLD = 5;
  private cleanupFns: (() => void)[] = [];

  ngAfterViewInit(): void {
    this.ngZone.runOutsideAngular(() => {
      const el = this.footTabRef?.nativeElement;
      if (!el) return;

      const onDown = (e: PointerEvent) => {
        this.dragging = true;
        this.movedPx = 0;
        this.startX = e.clientX - el.offsetLeft;
        this.scrollLeft = el.scrollLeft;
        el.setPointerCapture(e.pointerId);
        el.style.cursor = 'grabbing';
      };

      const onMove = (e: PointerEvent) => {
        if (!this.dragging) return;
        const dx = e.clientX - el.offsetLeft - this.startX;
        this.movedPx = Math.abs(dx);
        el.scrollLeft = this.scrollLeft - dx;
      };

      const onUp = () => {
        this.dragging = false;
        el.style.cursor = '';
      };

      const onClickCapture = (e: MouseEvent) => {
        if (this.movedPx > this.DRAG_THRESHOLD) e.preventDefault();
      };

      el.addEventListener('pointerdown', onDown);
      el.addEventListener('pointermove', onMove);
      el.addEventListener('pointerup', onUp);
      el.addEventListener('pointercancel', onUp);
      el.addEventListener('click', onClickCapture, true);

      this.cleanupFns = [
        () => el.removeEventListener('pointerdown', onDown),
        () => el.removeEventListener('pointermove', onMove),
        () => el.removeEventListener('pointerup', onUp),
        () => el.removeEventListener('pointercancel', onUp),
        () => el.removeEventListener('click', onClickCapture, true),
      ];
    });
  }

  ngOnDestroy(): void {
    this.cleanupFns.forEach(fn => fn());
  }

  protected toggleTheme(): void {
    this.theme.set(
      this.theme() === 'va-corporate' ? 'va-steel' : 'va-corporate'
    );
  }

  protected readonly navItems = [
    { label: 'Home', icon: 'home', route: '/home' },
    { label: 'Dashboard', icon: 'dashboard', route: '/dashboard' },
    { label: 'Settings', icon: 'settings', route: '/settings' },
    { label: 'Chemical Elements', icon: 'science', route: '/chemical-elements' },
  ];
}
