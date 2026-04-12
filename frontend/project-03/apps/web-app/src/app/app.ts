import {
  Component,
  OnInit,
  OnDestroy,
  inject,
  signal,
  computed,
  ViewChild,
  ElementRef,
  effect,
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
type RunStage = 'idle' | 'preparing' | 'installing' | 'starting' | 'running' | 'error';
type ResizeTarget = 'explorer' | 'editorSplit' | 'terminal';

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
  @ViewChild('ideShell') ideShellRef?: ElementRef<HTMLDivElement>;
  @ViewChild('workArea') workAreaRef?: ElementRef<HTMLDivElement>;

  // State
  readonly bootStatus = this.wc.bootStatus;
  readonly bootError = signal('');
  readonly previewUrl = this.wc.previewUrl;
  readonly fileTree = signal<FileNode[]>([]);
  readonly runStage = signal<RunStage>('idle');
  readonly runMessage = signal('');
  readonly runSeconds = signal(0);
  readonly explorerWidth = signal(220);
  readonly editorPaneWidth = signal(58);
  readonly terminalHeight = signal(220);
  readonly isResizing = signal(false);

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
  readonly ideGridColumns = computed(() => `48px ${this.explorerWidth()}px 4px 1fr`);

  private shellWriter: ((data: string) => void) | null = null;
  private shellKill: (() => void) | null = null;
  private runSecondsTimer: ReturnType<typeof setInterval> | null = null;
  private heartbeatTimer: ReturnType<typeof setInterval> | null = null;
  private removeResizeListeners: (() => void) | null = null;

  private readonly previewReadyEffect = effect(() => {
    const url = this.previewUrl();
    if (!url) return;
    if (this.runStage() === 'installing' || this.runStage() === 'starting' || this.runStage() === 'preparing') {
      this.runStage.set('running');
      this.runMessage.set('Dev server is running');
      this.stopProgressTimers();
      this.terminalRef?.writeLine('> Preview ready. App is running.');
      this.terminalRef?.writeLine(`> URL: ${url}`);
    }
  });

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
    this.stopProgressTimers();
    this.stopResize();
    this.shellKill?.();
    this.wc.teardown();
  }

  async loadTemplate(template: TemplateInfo): Promise<void> {
    this.selectedTemplate.set(template);
    this.showTemplateSelector.set(false);
    this.openFiles.set([]);
    this.activeFilePath.set('');
    this.terminalRef?.clear();
    this.runStage.set('preparing');
    this.runMessage.set('Loading template files');
    this.runSeconds.set(0);

    this.templatesService.getTemplate(template.id).subscribe({
      next: async (detail: TemplateDetail) => {
        await this.wc.loadTemplateFiles(detail.files);
        if (detail.files.length > 0) {
          this.openFile(detail.files[0].path, detail.files[0].content);
        }
        await this.runTemplateBootstrap(detail);
      },
      error: (err) => {
        const msg = err instanceof Error ? err.message : String(err);
        this.stopProgressTimers();
        this.runStage.set('error');
        this.runMessage.set(msg);
        this.terminalRef?.writeLine(`Failed to load template: ${msg}`);
      },
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

  private async runTemplateBootstrap(detail: TemplateDetail): Promise<void> {
    const hasPackageJson = detail.files.some((file) => file.path === 'package.json');
    if (!hasPackageJson) {
      this.runStage.set('idle');
      this.runMessage.set('No package.json found in template');
      return;
    }

    const startCommand = detail.framework === 'angular' ? 'npm run start' : 'npm run dev';
    this.bottomPanel.set('terminal');
    this.runStage.set('installing');
    this.runMessage.set('Installing dependencies');
    this.startProgressTimers();
    this.terminalRef?.writeLine('');
    this.terminalRef?.writeLine('> Preparing template workspace...');
    this.terminalRef?.writeLine('> Auto setup: npm install --no-audit --no-fund --no-progress');
    this.terminalRef?.writeLine(`> Auto run: ${startCommand}`);
    this.terminalRef?.writeLine('> Press Ctrl+C in terminal to stop the running app.');
    this.terminalRef?.writeLine('> Preview appears when the dev server reports ready.');

    if (!this.shellWriter) {
      await this.startShell();
    }

    const command = detail.framework === 'angular'
      ? 'npm install --no-audit --no-fund --no-progress && echo "[devbox] install done" && npm run start -- --no-progress\r'
      : 'npm install --no-audit --no-fund --no-progress && echo "[devbox] install done" && npm run dev\r';

    this.shellWriter?.(command);
  }

  private async startShell(): Promise<void> {
    try {
      const { write, kill } = await this.wc.spawnShell(
        (output) => {
          if (output.includes('[devbox] install done')) {
            this.runStage.set('starting');
            this.runMessage.set('Starting development server');
            this.terminalRef?.writeLine('> Dependencies installed. Starting dev server...');
          }

          const urlMatch = output.match(/https?:\/\/[^\s"'`]+/);
          if (urlMatch) {
            const detectedUrl = urlMatch[0];
            this.wc.previewUrl.set(detectedUrl);
            if (this.runStage() !== 'running') {
              this.runStage.set('running');
              this.runMessage.set('Dev server is running');
              this.stopProgressTimers();
              this.terminalRef?.writeLine(`> Preview detected from logs: ${detectedUrl}`);
            }
          }

          this.terminalRef?.write(output);
        },
        (cols, rows) => { /* handled by FitAddon */ },
      );
      this.shellWriter = write;
      this.shellKill = kill;
    } catch (e) {
      this.terminalRef?.writeLine('Shell not available in this environment.');
    }
  }

  private startProgressTimers(): void {
    this.stopProgressTimers();
    this.runSeconds.set(0);

    this.runSecondsTimer = setInterval(() => {
      this.runSeconds.update((s) => s + 1);
    }, 1000);

    this.heartbeatTimer = setInterval(() => {
      const stage = this.runStage();
      if (stage === 'running' || stage === 'idle' || stage === 'error') return;
      this.terminalRef?.writeLine(`> Still working (${stage})... ${this.runSeconds()}s elapsed`);
    }, 15000);
  }

  private stopProgressTimers(): void {
    if (this.runSecondsTimer) {
      clearInterval(this.runSecondsTimer);
      this.runSecondsTimer = null;
    }
    if (this.heartbeatTimer) {
      clearInterval(this.heartbeatTimer);
      this.heartbeatTimer = null;
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

  startResize(target: ResizeTarget, event: MouseEvent): void {
    event.preventDefault();
    this.stopResize();
    this.isResizing.set(true);

    const startX = event.clientX;
    const startY = event.clientY;
    const startExplorer = this.explorerWidth();
    const startTerminal = this.terminalHeight();

    const onMove = (moveEvent: MouseEvent) => {
      if (target === 'explorer') {
        const next = Math.min(520, Math.max(160, startExplorer + (moveEvent.clientX - startX)));
        this.explorerWidth.set(next);
        return;
      }

      if (target === 'editorSplit') {
        const el = this.workAreaRef?.nativeElement;
        if (!el) return;
        const rect = el.getBoundingClientRect();
        const pct = ((moveEvent.clientX - rect.left) / rect.width) * 100;
        this.editorPaneWidth.set(Math.min(80, Math.max(20, pct)));
        return;
      }

      const next = Math.min(520, Math.max(120, startTerminal + (startY - moveEvent.clientY)));
      this.terminalHeight.set(next);
    };

    const onUp = () => {
      this.stopResize();
    };

    window.addEventListener('mousemove', onMove);
    window.addEventListener('mouseup', onUp, { once: true });
    this.removeResizeListeners = () => {
      window.removeEventListener('mousemove', onMove);
      window.removeEventListener('mouseup', onUp);
    };
  }

  private stopResize(): void {
    this.removeResizeListeners?.();
    this.removeResizeListeners = null;
    this.isResizing.set(false);
  }
}
