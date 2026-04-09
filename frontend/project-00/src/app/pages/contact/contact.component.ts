import { Component } from '@angular/core';

@Component({
  selector: 'app-contact',
  standalone: true,
  template: `
    <div class="page-container">
      <h1>Contact Us</h1>
      <p>Get in touch with us using the contact form below.</p>
    </div>
  `,
  styles: [`
    .page-container {
      padding: 20px;
    }
  `]
})
export class ContactComponent { }
