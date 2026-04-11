import {
  Component,
  OnInit,
  OnDestroy,
  inject,
  signal,
  computed,
  ViewChild,
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { EditorComponent } from './components/editor/editor.component';
import { TerminalComponent } from './components/terminal/terminal.component';
import { FileTreeComponent } from './components/file-tree/file-tree.component';
import { PreviewComponent } from './components/preview/preview.component';
import { WebContainerService, FileNode } from './services/web-container.service';
import { ProjectTemplatesService, TemplateInfo, TemplateDetail } from './services/project-templates.service';

type Panel = 'editor' | 'preview' | 'split';
type BottomPanel = 'terminal' | 'packages' | 'hidden';

interface OpenFile {
  path: string;
  language: string;
  content: string;
  dirty: boolean;
}

function extToLanguage(name: string): string {
  const ext = name.split('.').pop()?.toLowerCase() ?? '';
  const map: Record<string, string> = {
    ts: 'typescript', tsx: 'typescriptreact', js: 'javascript', jsx: 'javascriptreact',
    html: 'html', css: 'css', scss: 'scss', json: 'json', md: 'markdown',
    vue: 'vue', py: 'python', sh: 'shell',
  };
  return map[ext] ?? 'plaintext';
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, EditorComponent, TerminalComponent, FileTreeComponent, PreviewComponent],
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class AppComponent implements OnInit, OnDestroy {
  protected wc = inject(WebContainerService);
  private templatesService = inject(ProjectTemplatesService);

  @ViewChild(TerminalComponent) terminalRef?: TerminalComponent;

  // State
  readonly bootStatus = this.wc.bootStatus;
  readonly bootError = signal('');
  readonly previewUrl = this.wc.previewUrl;
  readonly fileTree = signal<FileNode[]>([]);

  templates = signal<TemplateInfo[]>([]);
  selectedTemplate = signal<TemplateInfo | null>(null);
  openFiles = signal<OpenFile[]>([]);
  activeFilePath = signal<string>('');
  panel = signal<Panel>('split');
  bottomPanel = signal<BottomPanel>('terminal');
  showTemplateSelector = signal(false);
  packageQuery = signal('');
  packageResults = signal<{ name: string; version: string; description: string }[]>([]);

  readonly activeFile = computed(() =>
    this.openFiles().find(f => f.path === this.activeFilePath())
  );

  private shellWriter: ((data: string) => void) | null = null;
  private shellKill: (() => void) | null = null;

  async ngOnInit(): Promise<void> {
    this.templatesService.getTemplates().subscribe(t => this.templates.set(t));
    this.wc.fileTree$.subscribe(tree => this.fileTree.set(tree));

    try {
      await this.wc.boot();
      await this.startShell();
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      this.bootError.set(msg);
      this.terminalRef?.writeLine(`Boot error: ${msg}`);
      console.error('WebContainer boot failed:', e);
    }
  }

  ngOnDestroy(): void {
    this.shellKill?.();
    this.wc.teardown();
  }

  async loadTemplate(template: TemplateInfo): Promise<void> {
    this.selectedTemplate.set(template);
    this.showTemplateSelector.set(false);
    this.openFiles.set([]);
    this.activeFilePath.set('');
    this.terminalRef?.clear();

    this.templatesService.getTemplate(template.id).subscribe(async (detail: TemplateDetail) => {
      await this.wc.loadTemplateFiles(detail.files);
      if (detail.files.length > 0) {
        this.openFile(detail.files[0].path, detail.files[0].content);
      }
    });
  }

  async onFileSelected(path: string): Promise<void> {
    const existing = this.openFiles().find(f => f.path === path);
    if (existing) {
      this.activeFilePath.set(path);
      return;
    }
    try {
      const content = await this.wc.readFile(path);
      this.openFile(path, content);
    } catch {
      console.error('Failed to read file:', path);
    }
  }

  openFile(path: string, content: string): void {
    const name = path.split('/').pop() ?? path;
    this.openFiles.update(files => {
      if (files.find(f => f.path === path)) return files;
      return [...files, { path, language: extToLanguage(name), content, dirty: false }];
    });
    this.activeFilePath.set(path);
  }

  closeFile(path: string, event: MouseEvent): void {
    event.stopPropagation();
    this.openFiles.update(files => files.filter(f => f.path !== path));
    if (this.activeFilePath() === path) {
      const files = this.openFiles();
      this.activeFilePath.set(files.length > 0 ? files[files.length - 1].path : '');
    }
  }

  async onEditorValueChange(content: string): Promise<void> {
    const path = this.activeFilePath();
    if (!path) return;
    this.openFiles.update(files =>
      files.map(f => f.path === path ? { ...f, content, dirty: true } : f)
    );
    // Debounced write – simple approach
    await this.wc.writeFile(path, content);
    this.openFiles.update(files =>
      files.map(f => f.path === path ? { ...f, dirty: false } : f)
    );
  }

  async onFileDeleted(path: string): Promise<void> {
    await this.wc.deleteFile(path);
    this.closeFileByPath(path);
  }

  closeFileByPath(path: string): void {
    this.openFiles.update(files => files.filter(f => f.path !== path));
    if (this.activeFilePath() === path) {
      const files = this.openFiles();
      this.activeFilePath.set(files.length > 0 ? files[files.length - 1].path : '');
    }
  }

  onTerminalData(data: string): void {
    this.shellWriter?.(data);
  }

  private async startShell(): Promise<void> {
    try {
      const { write, kill } = await this.wc.spawnShell(
        (output) => this.terminalRef?.write(output),
        (cols, rows) => { /* handled by FitAddon */ },
      );
      this.shellWriter = write;
      this.shellKill = kill;
    } catch (e) {
      this.terminalRef?.writeLine('Shell not available in this environment.');
    }
  }

  togglePanel(p: Panel): void { this.panel.set(p); }
  toggleBottomPanel(p: BottomPanel): void {
    this.bottomPanel.set(this.bottomPanel() === p ? 'hidden' : p);
  }
  openTemplateSelector(): void { this.showTemplateSelector.set(true); }
  closeTemplateSelector(): void { this.showTemplateSelector.set(false); }

  getTabName(path: string): string { return path.split('/').pop() ?? path; }

  trackByPath(_: number, f: { path: string }): string { return f.path; }
}
