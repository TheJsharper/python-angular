import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-home',
  imports: [MatCardModule],
  template: `
    <mat-card>
      <mat-card-header>
        <mat-card-title>Home</mat-card-title>
        <mat-card-subtitle>Welcome to the application</mat-card-subtitle>
      </mat-card-header>
      <mat-card-content>
        @for (paragraph of paragraphs; track $index) {
          <p>{{ paragraph }}</p>
        }
      </mat-card-content>
    </mat-card>
  `,
})
export class HomeComponent {
  protected readonly paragraphs = Array.from(
    { length: 40 },
    (_, i) =>
      `${i + 1}. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.`
  );
}
