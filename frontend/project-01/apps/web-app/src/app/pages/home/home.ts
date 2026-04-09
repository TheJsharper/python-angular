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
        <p>This is the home page.</p>
      </mat-card-content>
    </mat-card>
  `,
})
export class HomeComponent {}
