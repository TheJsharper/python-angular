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
        <p>This is the dashboard page.</p>
      </mat-card-content>
    </mat-card>
  `,
})
export class DashboardComponent {}
