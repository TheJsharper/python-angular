import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, signal } from '@angular/core';
import { MatIconButton } from '@angular/material/button';
import { MatIcon } from '@angular/material/icon';
import { MatListItem, MatListItemIcon, MatListItemTitle, MatNavList } from '@angular/material/list';
import { MatSidenav, MatSidenavContainer, MatSidenavContent } from '@angular/material/sidenav';
import { MatToolbar } from '@angular/material/toolbar';
import { MatTooltip } from '@angular/material/tooltip';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

interface NavItem {
  label: string;
  icon: string;
  route: string;
}

@Component({
  selector: 'app-main',
  standalone: true,
  imports: [
    CommonModule,
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    MatToolbar,
    MatSidenavContainer,
    MatSidenav,
    MatSidenavContent,
    MatNavList,
    MatListItem,
    MatListItemIcon,
    MatListItemTitle,
    MatIcon,
    MatIconButton,
    MatTooltip,
  ],
  templateUrl: './main.html',
  styleUrls: ['./main.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Main {
  title = 'Material Sidenav + Toolbar';
  sidenavOpened = signal(true);
  isDarkMode = signal(true);

  navItems: NavItem[] = [
    { label: 'Home', icon: 'home', route: '/' },
    { label: 'About', icon: 'info', route: '/about' },
    { label: 'Services', icon: 'build', route: '/services' },
    { label: 'Contact', icon: 'mail', route: '/contact' },
  ];

  toggleSidenav() {
    this.sidenavOpened.update(v => !v);
  }

  toggleTheme() {
    this.isDarkMode.update(v => !v);
    document.body.classList.toggle('light-theme', !this.isDarkMode());
  }
}
