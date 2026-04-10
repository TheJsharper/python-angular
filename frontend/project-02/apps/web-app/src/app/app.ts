import { Component, computed, inject, signal } from '@angular/core';
import { NavigationEnd, Router, RouterModule } from '@angular/router';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatTabsModule } from '@angular/material/tabs';

interface NavItem {
  label: string;
  route: string;
  icon: string;
}

interface NavCategory {
  title: string;
  items: NavItem[];
}

@Component({
  selector: 'app-root',
  imports: [
    RouterModule,
    MatSidenavModule,
    MatToolbarModule,
    MatListModule,
    MatIconModule,
    MatButtonModule,
    MatDividerModule,
    MatTooltipModule,
    MatTabsModule,
  ],
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class App {
  private readonly router = inject(Router);

  protected sidenavOpen = signal(true);
  protected darkMode = signal(false);
  protected docsTabIndex = signal(3);
  protected currentUrl = signal(this.router.url);

  constructor() {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.currentUrl.set(event.urlAfterRedirects);
        this.docsTabIndex.set(3);
      }
    });
  }

  protected isComponentRoute = computed(() => this.currentUrl().startsWith('/components/'));

  protected currentComponentSlug = computed(() => {
    const parts = this.currentUrl().split('/').filter(Boolean);
    return parts.length >= 2 ? parts[1] : '';
  });

  protected currentComponentName = computed(() =>
    this.currentComponentSlug()
      .split('-')
      .filter(Boolean)
      .map(part => part.charAt(0).toUpperCase() + part.slice(1))
      .join(' ')
  );

  protected currentMaterialModule = computed(() => {
    const pascal = this.currentComponentSlug()
      .split('-')
      .filter(Boolean)
      .map(part => part.charAt(0).toUpperCase() + part.slice(1))
      .join('');
    return pascal ? `Mat${pascal}Module` : 'MatButtonModule';
  });

  protected materialDocsUrl = computed(() => {
    const slug = this.currentComponentSlug();
    return slug ? `https://material.angular.dev/components/${slug}/overview` : 'https://material.angular.dev/components';
  });

  protected sdkImportSnippet = computed(() => {
    const materialModule = this.currentMaterialModule();
    const slug = this.currentComponentSlug();
    return [
      `import { ${materialModule} } from '@angular/material/${slug}';`,
      '',
      '@Component({',
      '  standalone: true,',
      '  imports: [',
      `    ${materialModule}`,
      '  ],',
      '})',
      'export class ExampleFeature {}',
    ].join('\n');
  });

  protected toggleDark(): void {
    this.darkMode.update(v => !v);
  }

  protected readonly navCategories: NavCategory[] = [
    {
      title: 'Overview',
      items: [{ label: 'Home', route: '/home', icon: 'home' }],
    },
    {
      title: 'Form Controls',
      items: [
        { label: 'Autocomplete', route: '/components/autocomplete', icon: 'search' },
        { label: 'Checkbox', route: '/components/checkbox', icon: 'check_box' },
        { label: 'Datepicker', route: '/components/datepicker', icon: 'event' },
        { label: 'Form Field', route: '/components/form-field', icon: 'text_fields' },
        { label: 'Input', route: '/components/input', icon: 'edit' },
        { label: 'Radio', route: '/components/radio', icon: 'radio_button_checked' },
        { label: 'Select', route: '/components/select', icon: 'expand_circle_down' },
        { label: 'Slide Toggle', route: '/components/slide-toggle', icon: 'toggle_on' },
      ],
    },
    {
      title: 'Navigation',
      items: [
        { label: 'Menu', route: '/components/menu', icon: 'menu_open' },
        { label: 'Paginator', route: '/components/paginator', icon: 'last_page' },
        { label: 'Tabs', route: '/components/tabs', icon: 'tab' },
      ],
    },
    {
      title: 'Layout',
      items: [
        { label: 'Card', route: '/components/card', icon: 'credit_card' },
        { label: 'Divider', route: '/components/divider', icon: 'remove' },
        { label: 'Expansion', route: '/components/expansion', icon: 'expand_more' },
        { label: 'List', route: '/components/list', icon: 'list' },
        { label: 'Stepper', route: '/components/stepper', icon: 'linear_scale' },
      ],
    },
    {
      title: 'Buttons & Indicators',
      items: [
        { label: 'Badge', route: '/components/badge', icon: 'notifications' },
        { label: 'Button', route: '/components/button', icon: 'smart_button' },
        { label: 'Button Toggle', route: '/components/button-toggle', icon: 'toggle_on' },
        { label: 'Chips', route: '/components/chips', icon: 'label' },
        { label: 'Icon', route: '/components/icon', icon: 'star' },
        { label: 'Progress Bar', route: '/components/progress-bar', icon: 'linear_scale' },
        { label: 'Progress Spinner', route: '/components/progress-spinner', icon: 'sync' },
      ],
    },
    {
      title: 'Popups & Modals',
      items: [
        { label: 'Bottom Sheet', route: '/components/bottom-sheet', icon: 'vertical_align_bottom' },
        { label: 'Dialog', route: '/components/dialog', icon: 'open_in_new' },
        { label: 'Snack Bar', route: '/components/snack-bar', icon: 'notifications_active' },
        { label: 'Tooltip', route: '/components/tooltip', icon: 'info' },
      ],
    },
    {
      title: 'Data Table',
      items: [
        { label: 'Table', route: '/components/table', icon: 'table_chart' },
      ],
    },
  ];
}
