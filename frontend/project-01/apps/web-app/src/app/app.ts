import { Component, signal } from '@angular/core';
import { RouterModule } from '@angular/router';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatTooltipModule } from '@angular/material/tooltip';

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const THEMES = ['va-corporate', 'va-steel'] as const;
type Theme = typeof THEMES[number];

@Component({
  imports: [
    RouterModule,
    MatSidenavModule,
    MatToolbarModule,
    MatListModule,
    MatIconModule,
    MatButtonModule,
    MatTooltipModule,
  ],
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class App {
  protected title = 'VA App';
  protected theme = signal<Theme>('va-corporate');

  protected toggleTheme(): void {
    this.theme.set(
      this.theme() === 'va-corporate' ? 'va-steel' : 'va-corporate'
    );
  }

  protected readonly navItems = [
    { label: 'Home', icon: 'home', route: '/home' },
    { label: 'Dashboard', icon: 'dashboard', route: '/dashboard' },
    { label: 'Settings', icon: 'settings', route: '/settings' },
  ];
}
