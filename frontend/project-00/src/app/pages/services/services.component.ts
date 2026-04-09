import { Component } from '@angular/core';

@Component({
  selector: 'app-services',
  standalone: true,
  template: `
    <div class="page-container">
      <h1>Services</h1>
      <p>Discover our services and what we offer.</p>
    </div>
  `,
  styles: [`
    .page-container {
      padding: 20px;
    }
  `]
})
export class ServicesComponent { }
