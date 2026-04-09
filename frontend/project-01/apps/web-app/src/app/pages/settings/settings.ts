import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-settings',
  imports: [MatCardModule],
  template: `
    <mat-card>
      <mat-card-header>
        <mat-card-title>Settings</mat-card-title>
        <mat-card-subtitle>Configure your preferences</mat-card-subtitle>
      </mat-card-header>
      <mat-card-content>
        @for (paragraph of paragraphs; track $index) {
          <p>{{ paragraph }}</p>
        }
      </mat-card-content>
    </mat-card>
  `,
})
export class SettingsComponent {
  protected readonly paragraphs = Array.from(
    { length: 40 },
    (_, i) =>
      `${i + 1}. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.`
  );
}
