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
import { MATERIAL_API_SNIPPETS } from './material-api-snippets';

interface NavItem {
  label: string;
  route: string;
  icon: string;
}

interface NavCategory {
  title: string;
  items: NavItem[];
}

interface ApiGroup {
  title: string;
  items: string[];
}

interface ApiEntityDetail {
  name: string;
  kind: string;
  description: string;
  signature: string;
  selector: string;
  exportedAs: string;
  properties: ApiMember[];
  methods: ApiMember[];
}

interface ApiMember {
  name: string;
  signature: string;
  description: string;
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
  protected selectedApiItem = signal<string | null>(null);

  constructor() {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.currentUrl.set(event.urlAfterRedirects);
        this.docsTabIndex.set(3);
        this.showCodePanel.set(false);
        this.activeCodeTab.set('html');
        this.copiedCode.set(false);
        this.selectedApiItem.set(null);
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

  protected currentApiData = computed(() => {
    const slug = this.currentComponentSlug();
    return MATERIAL_API_SNIPPETS[slug];
  });

  protected isTableApiPage = computed(() => this.currentComponentSlug() === 'table');

  protected readonly tableApiGroups: ApiGroup[] = [
    { title: 'Components', items: ['CdkTable', 'CdkHeaderRow', 'CdkFooterRow', 'CdkRow', 'CdkTextColumn'] },
    {
      title: 'Directives',
      items: [
        'CdkRecycleRows',
        'CdkCellDef',
        'CdkHeaderCellDef',
        'CdkFooterCellDef',
        'CdkColumnDef',
        'CdkHeaderCell',
        'CdkFooterCell',
        'CdkCell',
        'CdkHeaderRowDef',
        'CdkFooterRowDef',
        'CdkRowDef',
        'CdkNoDataRow',
      ],
    },
    { title: 'Classes', items: ['BaseCdkCell', 'BaseRowDef'] },
    {
      title: 'Interfaces',
      items: [
        'RowOutlet',
        'CellDef',
        'CdkCellOutletRowContext',
        'CdkCellOutletMultiRowContext',
        'StickyUpdate',
        'StickyPositioningListener',
        'TextColumnOptions',
      ],
    },
    { title: 'Type aliases', items: ['CdkTableDataSourceInput', 'StickySize', 'StickyOffset'] },
    { title: 'Constants', items: ['CDK_ROW_TEMPLATE', 'STICKY_POSITIONING_LISTENER', 'TEXT_COLUMN_OPTIONS'] },
  ];

  protected tableApiEntityMap = computed<Record<string, ApiEntityDetail>>(() => {
    if (!this.isTableApiPage()) {
      return {};
    }
    return this.buildTableApiEntityMap(this.apiTypeDefinitionsSnippet());
  });

  protected selectedTableApiDetail = computed<ApiEntityDetail | null>(() => {
    const entities = this.tableApiEntityMap();
    const selected = this.selectedApiItem();
    if (selected && entities[selected]) {
      return entities[selected];
    }

    const prioritized = this.flattenTableApiItems();
    for (const item of prioritized) {
      if (entities[item]) {
        return entities[item];
      }
    }

    return null;
  });

  protected apiTypeDefinitionsSnippet = computed(() => {
    const data = this.currentApiData();
    return data?.typeDefinitions || '// Type definitions not found in node_modules for this entry.';
  });

  protected apiScssSnippet = computed(() => {
    const data = this.currentApiData();
    return data?.scssPreview || '// SCSS files not found for this component in node_modules.';
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

  protected highlightTs(source: string): string {
    const grammar = Prism.languages['typescript'];
    return grammar ? Prism.highlight(source, grammar, 'typescript') : source;
  }

  protected highlightCss(source: string): string {
    const grammar = Prism.languages['css'];
    return grammar ? Prism.highlight(source, grammar, 'css') : source;
  }

  protected selectTableApiItem(item: string): void {
    this.selectedApiItem.set(item);
  }

  protected isSelectedTableApiItem(item: string): boolean {
    return this.selectedTableApiDetail()?.name === item;
  }

  private flattenTableApiItems(): string[] {
    return this.tableApiGroups.flatMap(group => group.items);
  }

  private buildTableApiEntityMap(typeDefinitions: string): Record<string, ApiEntityDetail> {
    const entities: Record<string, ApiEntityDetail> = {};
    const lines = typeDefinitions.split('\n');
    const kindByName = new Map(this.tableApiGroups.flatMap(group => group.items.map(item => [item, group.title])));

    for (const name of this.flattenTableApiItems()) {
      const declarationLine = this.findDeclarationLine(lines, name);
      if (!declarationLine) {
        continue;
      }

      const lineText = lines[declarationLine].trim();
      const block = this.extractDeclarationBlock(lines, declarationLine);
      const members = block
        ? this.extractMembersFromBlock(lines, block.startLine + 1, block.endLine)
        : { properties: [], methods: [] };

      entities[name] = {
        name,
        kind: this.resolveEntityKind(lineText, kindByName.get(name) || ''),
        description: this.extractNearestJsDoc(lines, declarationLine),
        signature: lineText,
        selector: this.getTableSelector(name),
        exportedAs: this.getTableExportedAs(name),
        properties: members.properties,
        methods: members.methods,
      };
    }

    return entities;
  }

  private findDeclarationLine(lines: string[], name: string): number | null {
    const directDeclaration = new RegExp(
      `^\\s*(?:export\\s+)?(?:declare\\s+)?(?:abstract\\s+)?(?:class|interface|type|const)\\s+${name}\\b`
    );

    for (let i = 0; i < lines.length; i += 1) {
      if (directDeclaration.test(lines[i])) {
        return i;
      }
    }

    const exportLine = new RegExp(`^\\s*export\\s*\\{[^}]*\\b${name}\\b[^}]*\\}`);
    for (let i = 0; i < lines.length; i += 1) {
      if (exportLine.test(lines[i])) {
        return i;
      }
    }

    return null;
  }

  private resolveEntityKind(signature: string, fallbackGroup: string): string {
    if (signature.includes(' class ')) {
      return 'Class';
    }
    if (signature.includes(' interface ')) {
      return 'Interface';
    }
    if (signature.includes(' type ')) {
      return 'Type alias';
    }
    if (signature.includes(' const ')) {
      return 'Constant';
    }

    if (fallbackGroup === 'Components' || fallbackGroup === 'Directives' || fallbackGroup === 'Classes') {
      return 'Class';
    }
    if (fallbackGroup === 'Interfaces') {
      return 'Interface';
    }
    if (fallbackGroup === 'Type aliases') {
      return 'Type alias';
    }
    if (fallbackGroup === 'Constants') {
      return 'Constant';
    }

    return 'API symbol';
  }

  private getTableSelector(name: string): string {
    const selectorMap: Record<string, string> = {
      CdkTable: 'cdk-table, table[cdk-table]',
      CdkHeaderRow: 'cdk-header-row, tr[cdk-header-row]',
      CdkFooterRow: 'cdk-footer-row, tr[cdk-footer-row]',
      CdkRow: 'cdk-row, tr[cdk-row]',
      CdkCell: 'cdk-cell, td[cdk-cell]',
      CdkHeaderCell: 'cdk-header-cell, th[cdk-header-cell]',
      CdkFooterCell: 'cdk-footer-cell, td[cdk-footer-cell]',
      CdkCellDef: '[cdkCellDef]',
      CdkHeaderCellDef: '[cdkHeaderCellDef]',
      CdkFooterCellDef: '[cdkFooterCellDef]',
      CdkColumnDef: '[cdkColumnDef]',
      CdkHeaderRowDef: '[cdkHeaderRowDef]',
      CdkFooterRowDef: '[cdkFooterRowDef]',
      CdkRowDef: '[cdkRowDef]',
      CdkNoDataRow: '[cdkNoDataRow]',
      CdkTextColumn: 'cdk-text-column',
    };

    return selectorMap[name] || 'N/A (local type metadata)';
  }

  private getTableExportedAs(name: string): string {
    if (!name) {
      return '-';
    }
    return name.charAt(0).toLowerCase() + name.slice(1);
  }

  private extractDeclarationBlock(
    lines: string[],
    declarationLine: number
  ): { startLine: number; endLine: number } | null {
    let openLine = declarationLine;
    while (openLine < lines.length && !lines[openLine].includes('{')) {
      openLine += 1;
    }

    if (openLine >= lines.length) {
      return null;
    }

    let depth = 0;
    let started = false;
    for (let i = openLine; i < lines.length; i += 1) {
      for (const ch of lines[i]) {
        if (ch === '{') {
          depth += 1;
          started = true;
        } else if (ch === '}') {
          depth -= 1;
          if (started && depth === 0) {
            return { startLine: openLine, endLine: i };
          }
        }
      }
    }

    return null;
  }

  private extractMembersFromBlock(
    lines: string[],
    startLine: number,
    endLine: number
  ): { properties: ApiMember[]; methods: ApiMember[] } {
    const properties: ApiMember[] = [];
    const methods: ApiMember[] = [];

    for (let i = startLine; i < endLine; i += 1) {
      const raw = lines[i].trim();
      if (!raw || raw.startsWith('//') || raw.startsWith('*') || raw.startsWith('/**')) {
        continue;
      }

      if (
        raw.startsWith('private ') ||
        raw.startsWith('protected ') ||
        raw.startsWith('static ') ||
        raw.startsWith('constructor(') ||
        raw.startsWith('set ') ||
        raw.startsWith('get ') ||
        raw.startsWith('_')
      ) {
        continue;
      }

      const signature = this.normalizeMemberSignature(raw);
      if (!signature || !signature.endsWith(';')) {
        continue;
      }

      const description = this.extractNearestJsDoc(lines, i);
      const methodMatch = signature.match(/^([A-Za-z_$][\w$]*)\s*\(/);
      const propertyMatch = signature.match(/^([A-Za-z_$][\w$]*)\??\s*:/);

      if (methodMatch) {
        methods.push({
          name: methodMatch[1],
          signature,
          description,
        });
      } else if (propertyMatch) {
        properties.push({
          name: propertyMatch[1],
          signature,
          description,
        });
      }
    }

    return { properties, methods };
  }

  private normalizeMemberSignature(line: string): string {
    return line
      .replace(/^(public|readonly|override|abstract|declare)\s+/g, '')
      .replace(/\s+/g, ' ')
      .trim();
  }

  private extractNearestJsDoc(lines: string[], declarationLine: number): string {
    let cursor = declarationLine - 1;
    while (cursor >= 0 && lines[cursor].trim() === '') {
      cursor -= 1;
    }

    if (cursor < 0 || !lines[cursor].includes('*/')) {
      return 'Description loaded from local node_modules type definitions.';
    }

    const commentLines: string[] = [];
    while (cursor >= 0) {
      const line = lines[cursor].trim();
      commentLines.unshift(line);
      if (line.includes('/**')) {
        break;
      }
      cursor -= 1;
    }

    const text = commentLines
      .map(line => line.replace(/^\/\*\*\s?/, '').replace(/^\*\/?\s?/, '').replace(/\*\/$/, '').trim())
      .filter(Boolean)
      .join(' ')
      .trim();

    return text || 'Description loaded from local node_modules type definitions.';
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
