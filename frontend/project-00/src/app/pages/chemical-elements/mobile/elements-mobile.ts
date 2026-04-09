import { Component, signal } from '@angular/core';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatListModule } from '@angular/material/list';
import { MatDividerModule } from '@angular/material/divider';
import { ELEMENT_DATA, PeriodicElement } from '../element-data';

@Component({
  selector: 'app-elements-mobile',
  standalone: true,
  imports: [MatListModule, MatIconModule, MatButtonModule, MatDividerModule],
  templateUrl: './elements-mobile.html',
  styleUrls: ['./elements-mobile.scss'],
})
export class ElementsMobileComponent {
  readonly elements = ELEMENT_DATA;
  selected = signal<PeriodicElement | null>(null);

  select(el: PeriodicElement): void {
    this.selected.set(el);
  }

  back(): void {
    this.selected.set(null);
  }
}
