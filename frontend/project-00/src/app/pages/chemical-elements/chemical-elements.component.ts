import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { BreakpointObserver } from '@angular/cdk/layout';
import { map } from 'rxjs';
import { ElementsTableComponent } from './desktop/elements-table';
import { ElementsMobileComponent } from './mobile/elements-mobile';

@Component({
  selector: 'app-chemical-elements',
  standalone: true,
  imports: [ElementsTableComponent, ElementsMobileComponent],
  templateUrl: './chemical-elements.component.html',
  styleUrls: ['./chemical-elements.component.scss'],
})
export class ChemicalElementsComponent {
  private readonly breakpoint = inject(BreakpointObserver);

  readonly isMobile = toSignal(
    this.breakpoint.observe('(max-width: 768px)').pipe(map(r => r.matches)),
    { initialValue: false }
  );
}
