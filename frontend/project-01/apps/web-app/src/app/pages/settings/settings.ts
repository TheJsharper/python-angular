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
        <p>This is the settings page.</p>
      </mat-card-content>
    </mat-card>
  `,
})
export class SettingsComponent {}
