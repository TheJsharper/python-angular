import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  standalone: true,
  template: `
    <div class="page-container">
      <h1>Welcome Home</h1>
      <p>This is the home page of your Material sidenav + toolbar application.</p>
    </div>
  `,
  styles: [`
    .page-container {
      padding: 20px;
    }
  `]
})
export class HomeComponent { }
