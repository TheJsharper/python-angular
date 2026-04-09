import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-dashboard',
  imports: [MatCardModule],
  template: `
    <mat-card>
      <mat-card-header>
        <mat-card-title>Dashboard</mat-card-title>
        <mat-card-subtitle>Overview of your data</mat-card-subtitle>
      </mat-card-header>
      <mat-card-content>
        @for (paragraph of paragraphs; track $index) {
          <p>{{ paragraph }}</p>
        }
      </mat-card-content>
    </mat-card>
  `,
})
export class DashboardComponent {
  protected readonly paragraphs = Array.from(
    { length: 40 },
    (_, i) =>
      `${i + 1}. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc viverra, mauris vel suscipit cursus, velit velit placerat justo, sed luctus sapien lorem at neque. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.`
  );
}
