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
import Prism from 'prismjs';
import 'prismjs/components/prism-markup';
import 'prismjs/components/prism-clike';
import 'prismjs/components/prism-javascript';
import 'prismjs/components/prism-typescript';
import 'prismjs/components/prism-css';
import { EXAMPLE_SNIPPETS } from './example-snippets';

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
  styleUrls: ['./app.scss'],
})
export class App {
  private readonly router = inject(Router);

  protected sidenavOpen = signal(true);
  protected darkMode = signal(false);
  protected docsTabIndex = signal(3);
  protected currentUrl = signal(this.router.url);
  protected showCodePanel = signal(false);
  protected activeCodeTab = signal<'html' | 'ts' | 'css'>('html');
  protected copiedCode = signal(false);

  constructor() {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.currentUrl.set(event.urlAfterRedirects);
        this.docsTabIndex.set(3);
        this.showCodePanel.set(false);
        this.activeCodeTab.set('html');
        this.copiedCode.set(false);
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

  protected materialExamplesUrl = computed(() => {
    const slug = this.currentComponentSlug();
    if (!slug) {
      return 'https://material.angular.dev/components';
    }
    if (slug === 'table') {
      return 'https://material.angular.dev/cdk/table/examples';
    }
    return `https://material.angular.dev/components/${slug}/examples`;
  });

  protected selectorName = computed(() => {
    const slug = this.currentComponentSlug();
    return slug ? `lib-${slug}` : 'lib-component';
  });

  protected exampleHtmlSnippet = computed(() => {
    const slug = this.currentComponentSlug();
    const registryEntry = EXAMPLE_SNIPPETS[slug];
    if (registryEntry?.html) {
      return registryEntry.html;
    }

    const selector = this.selectorName();
    return [
      `<section class="example-shell">`,
      `  <${selector}></${selector}>`,
      `</section>`,
    ].join('\n');
  });

  protected exampleTsSnippet = computed(() => {
    const slug = this.currentComponentSlug();
    const registryEntry = EXAMPLE_SNIPPETS[slug];
    if (registryEntry?.ts) {
      return this.normalizeTsTemplateDisplay(registryEntry.ts, slug);
    }

    const featureName = this.currentComponentName().replace(/\s+/g, '');
    const importAlias = `@project-02/views-${slug === 'table' ? 'table' : slug === 'menu' || slug === 'paginator' || slug === 'tabs' ? 'navigation' : slug === 'card' || slug === 'divider' || slug === 'expansion' || slug === 'list' || slug === 'stepper' ? 'layout' : slug === 'bottom-sheet' || slug === 'dialog' || slug === 'snack-bar' || slug === 'tooltip' ? 'overlays' : slug === 'badge' || slug === 'button' || slug === 'button-toggle' || slug === 'chips' || slug === 'icon' || slug === 'progress-bar' || slug === 'progress-spinner' ? 'indicators' : 'form-controls'}`;
    const componentName = `${featureName}Component`;

    return [
      `import { Component } from '@angular/core';`,
      `import { ${componentName} } from '${importAlias}';`,
      ``,
      `@Component({`,
      `  selector: 'app-example-host',`,
      `  standalone: true,`,
      `  imports: [${componentName}],`,
      `  templateUrl: './example-host.html',`,
      `})`,
      `export class ExampleHostComponent {}`,
    ].join('\n');
  });

  private normalizeTsTemplateDisplay(tsCode: string, slug: string): string {
    const templateBlock = /\n\s*template\s*:\s*`[\s\S]*?`\s*,/m;
    if (!templateBlock.test(tsCode)) {
      return tsCode;
    }

    return tsCode.replace(
      templateBlock,
      `\n  templateUrl: './${slug}.html',`
    );
  }

  protected exampleCssSnippet = computed(() => {
    const slug = this.currentComponentSlug();
    const registryEntry = EXAMPLE_SNIPPETS[slug];
    if (registryEntry?.css) {
      return registryEntry.css;
    }

    return [
      `.example-shell {`,
      `  padding: 16px;`,
      `  border: 1px solid var(--mat-sys-outline-variant);`,
      `  border-radius: 12px;`,
      `}`,
    ].join('\n');
  });

  protected activeSnippet = computed(() => {
    const tab = this.activeCodeTab();
    if (tab === 'ts') {
      return this.exampleTsSnippet();
    }
    if (tab === 'css') {
      return this.exampleCssSnippet();
    }
    return this.exampleHtmlSnippet();
  });

  protected highlightedSnippet = computed(() => {
    const source = this.activeSnippet();
    const tab = this.activeCodeTab();
    const language = tab === 'html' ? 'markup' : tab === 'ts' ? 'typescript' : 'css';
    const grammar = Prism.languages[language];
    if (!grammar) {
      return source;
    }

    const highlighted = Prism.highlight(source, grammar, language);
    return tab === 'html' ? this.normalizeMarkupSpacing(highlighted) : highlighted;
  });

  private normalizeMarkupSpacing(highlighted: string): string {
    // Prism may emit attribute tokens without a preserved leading space for Angular-style attrs.
    // Prefix each attr token with a non-breaking space so markup always renders as `<tag attr="...">`.
    return highlighted.replace(/<span class="token attr-name">/g, '&nbsp;<span class="token attr-name">');
  }

  protected toggleCodePanel(): void {
    this.showCodePanel.update(v => !v);
  }

  protected setCodeTab(tab: 'html' | 'ts' | 'css'): void {
    this.activeCodeTab.set(tab);
  }

  protected async copyActiveSnippet(): Promise<void> {
    await navigator.clipboard.writeText(this.activeSnippet());
    this.copiedCode.set(true);
    setTimeout(() => this.copiedCode.set(false), 1400);
  }

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
