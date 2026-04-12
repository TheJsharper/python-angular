import {
  Component,
  OnInit,
  AfterViewInit,
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
type BottomPanel = 'terminal' | 'packages' | 'logs' | 'hidden';
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
export class AppComponent implements OnInit, AfterViewInit, OnDestroy {
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
  templatesLoading = signal(false);
  templatesError = signal('');
  selectedTemplate = signal<TemplateInfo | null>(null);
  openFiles = signal<OpenFile[]>([]);
  activeFilePath = signal<string>('');
  panel = signal<Panel>('split');
  bottomPanel = signal<BottomPanel>('terminal');
  showTemplateSelector = signal(false);
  packageQuery = signal('');
  packageResults = signal<{ name: string; version: string; description: string }[]>([]);
  runLogs = signal<string[]>([]);
  readonly templateActionInProgress = computed(() => {
    const stage = this.runStage();
    return stage === 'preparing' || stage === 'installing';
  });
  readonly recentRunLogs = computed(() => this.runLogs().slice(-200));

  readonly activeFile = computed(() =>
    this.openFiles().find(f => f.path === this.activeFilePath())
  );
  readonly ideGridColumns = computed(() => `48px ${this.explorerWidth()}px 4px 1fr`);

  private shellWriter: ((data: string) => void) | null = null;
  private shellKill: (() => void) | null = null;
  private runSecondsTimer: ReturnType<typeof setInterval> | null = null;
  private heartbeatTimer: ReturnType<typeof setInterval> | null = null;
  private startWatchdogTimer: ReturnType<typeof setTimeout> | null = null;
  private removeResizeListeners: (() => void) | null = null;
  private pendingTerminalOutput: Array<{ text: string; line: boolean }> = [];
  private logChunkBuffer = '';

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
    this.loadTemplates();
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

  ngAfterViewInit(): void {
    if (!this.terminalRef || this.pendingTerminalOutput.length === 0) return;
    for (const entry of this.pendingTerminalOutput) {
      if (entry.line) {
        this.terminalRef.writeLine(entry.text);
      } else {
        this.terminalRef.write(entry.text);
      }
    }
    this.pendingTerminalOutput = [];
  }

  ngOnDestroy(): void {
    this.stopProgressTimers();
    this.stopResize();
    this.shellKill?.();
    this.wc.teardown();
  }

  async loadTemplate(template: TemplateInfo): Promise<void> {
    if (this.templateActionInProgress()) {
      this.writeTerminal('> A template action is already in progress. Please wait...', true);
      return;
    }

    this.clearRunLogs('Template run started');
    this.selectedTemplate.set(template);
    this.showTemplateSelector.set(false);
    this.openFiles.set([]);
    this.activeFilePath.set('');
    this.terminalRef?.clear();
    this.runStage.set('preparing');
    this.runMessage.set('Loading template files');
    this.runSeconds.set(0);

    if (template.framework === 'angular') {
      await this.bootstrapAngularCliTemplate();
      return;
    }

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
        this.writeTerminal(`Failed to load template: ${msg}`, true);
      },
    });
  }

  private async bootstrapAngularCliTemplate(): Promise<void> {
    if (!this.shellWriter) {
      await this.startShell();
    }

    await this.wc.loadTemplateFiles([]);
    this.bottomPanel.set('terminal');
    this.runStage.set('preparing');
    this.runMessage.set('Scaffolding Angular CLI project');
    this.startProgressTimers();
    this.writeTerminal('> Scaffolding Angular app with @angular/cli...', true);
    this.writeTerminal('> Step 1/2: create project-template-angular/', true);
    this.writeTerminal('> Step 2/3: install all packages (verbose)', true);
    this.writeTerminal('> Step 3/3: start Angular dev server automatically', true);
    this.writeTerminal('> Full logs will stream in terminal.', true);

    const command =
      'echo "[devbox] create start"\n' +
      'rm -rf project-template-angular\n' +
      'npm_config_yes=true npm_config_color=false npm_config_progress=false CI=true npx -y @angular/cli@latest new project-template-angular --defaults --skip-git --skip-install --routing --style=scss --standalone --package-manager=npm\n' +
      'if [ $? -ne 0 ]; then echo "[devbox] create failed"; fi\n' +
      'if [ -d project-template-angular ]; then echo "[devbox] ngnew done"; fi\n' +
      'if [ -d project-template-angular ]; then cd project-template-angular; fi\n' +
      'echo "[devbox] install start"\n' +
      'npm_config_yes=true npm_config_color=false npm_config_progress=false CI=true npm install --verbose --no-audit --no-fund --no-progress\n' +
      'if [ $? -ne 0 ]; then echo "[devbox] install failed"; else echo "[devbox] install done"; fi\n' +
      'if [ -d project-template-angular ]; then echo "[devbox] start dev"; npm run start -- --host 0.0.0.0 --port 4200 --no-progress || echo "[devbox] start failed"; fi\r';

    this.writeTerminal('> Shell connected. Running scaffold and install commands...', true);
    this.shellWriter?.(command);
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
    this.writeTerminal('', true);
    this.writeTerminal('> Preparing template workspace...', true);
    this.writeTerminal('> Auto setup: npm install --verbose --no-audit --no-fund --no-progress', true);
    this.writeTerminal(`> Auto run: ${startCommand}`, true);
    this.writeTerminal('> Press Ctrl+C in terminal to stop the running app.', true);
    this.writeTerminal('> Preview appears when the dev server reports ready.', true);

    if (!this.shellWriter) {
      await this.startShell();
    }

    const command = detail.framework === 'angular'
      ? 'npm install --verbose --no-audit --no-fund --no-progress && echo "[devbox] install done" && npm run start -- --no-progress\r'
      : 'npm install --verbose --no-audit --no-fund --no-progress && echo "[devbox] install done" && npm run dev\r';

    this.shellWriter?.(command);
  }

  private async startShell(): Promise<void> {
    try {
      const { write, kill } = await this.wc.spawnShell(
        (output) => {
          if (output.includes('[devbox] create start')) {
            this.runStage.set('preparing');
            this.runMessage.set('Creating Angular project');
            this.writeTerminal('> Creating Angular CLI project...', true);
          }

          if (output.includes('[devbox] ngnew done')) {
            this.runStage.set('installing');
            this.runMessage.set('Installing dependencies (verbose)');
            this.writeTerminal('> Angular project scaffold created. Installing dependencies...', true);
            void this.wc.refreshFileTree();
          }

          if (output.includes('[devbox] create failed')) {
            this.stopProgressTimers();
            this.runStage.set('error');
            this.runMessage.set('Angular project creation failed');
            this.writeTerminal('> Angular CLI create failed. Check npm errors above.', true);
          }

          if (output.includes('[devbox] install start')) {
            this.runStage.set('installing');
            this.runMessage.set('Installing dependencies (verbose)');
            this.writeTerminal('> npm install --verbose started...', true);
          }

          if (output.includes('[devbox] install done')) {
            this.runStage.set('starting');
            this.runMessage.set('Starting development server');
            this.startStartWatchdog();
            this.writeTerminal('> Dependencies installed. Starting dev server...', true);
            void this.wc.refreshFileTree();
            void this.openPreferredWorkspaceFile();
            this.bottomPanel.set('terminal');
            setTimeout(() => {
              this.terminalRef?.refresh();
              this.terminalRef?.focus();
            }, 100);
          }

          if (output.includes('[devbox] start dev')) {
            this.runStage.set('starting');
            this.runMessage.set('Starting development server');
            this.startStartWatchdog();
            this.writeTerminal('> Launching dev server...', true);
          }

          if (output.includes('[devbox] start failed')) {
            this.stopProgressTimers();
            this.runStage.set('error');
            this.runMessage.set('Failed to start development server');
            this.writeTerminal('> Dev server failed to start. Check errors above.', true);
          }

          if (output.includes('[devbox] install failed')) {
            this.stopProgressTimers();
            this.runStage.set('error');
            this.runMessage.set('Dependency installation failed');
            this.writeTerminal('> npm install failed. Check npm errors above.', true);
            this.bottomPanel.set('terminal');
            setTimeout(() => {
              this.terminalRef?.refresh();
              this.terminalRef?.focus();
            }, 100);
          }

          const urlMatch = output.match(/https?:\/\/[^\s"'`]+/);
          if (urlMatch) {
            try {
              const detected = new URL(urlMatch[0]);
              const host = detected.hostname.toLowerCase();
              const isPreviewHost =
                host.endsWith('.webcontainer.io') ||
                host.endsWith('.webcontainer-api.io');

              if (isPreviewHost) {
                const detectedUrl = detected.href;
                this.wc.previewUrl.set(detectedUrl);
                if (this.runStage() !== 'running') {
                  this.runStage.set('running');
                  this.runMessage.set('Dev server is running');
                  this.clearStartWatchdog();
                  this.stopProgressTimers();
                  this.writeTerminal(`> Preview detected from logs: ${detectedUrl}`, true);
                }
              } else if (host === 'localhost' || host === '127.0.0.1') {
                this.writeTerminal('> Ignoring localhost preview URL from logs. Waiting for WebContainer public URL...', true);
              }
            } catch {
              // Ignore malformed URL fragments from terminal escape sequences.
            }
          }

          this.writeTerminal(output);
        },
        (cols, rows) => { /* handled by FitAddon */ },
      );
      this.shellWriter = write;
      this.shellKill = kill;
      this.writeTerminal('> Shell session ready.', true);
      this.shellWriter('\r');
      setTimeout(() => this.terminalRef?.refresh(), 50);
    } catch (e) {
      this.writeTerminal('Shell not available in this environment.', true);
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
      this.writeTerminal(`> Still working (${stage})... ${this.runSeconds()}s elapsed`, true);
    }, 5000);
  }

  private stopProgressTimers(): void {
    this.clearStartWatchdog();
    if (this.runSecondsTimer) {
      clearInterval(this.runSecondsTimer);
      this.runSecondsTimer = null;
    }
    if (this.heartbeatTimer) {
      clearInterval(this.heartbeatTimer);
      this.heartbeatTimer = null;
    }
  }

  async newTerminal(): Promise<void> {
    this.stopProgressTimers();
    this.runStage.set('idle');
    this.runMessage.set('Terminal ready');
    this.bottomPanel.set('terminal');

    const existingWriter = this.shellWriter;

    if (!existingWriter) {
      this.terminalRef?.clear();
      await this.startShell();
      this.writeTerminal('> New terminal ready. Type your command and press Enter.', true);
      const writerAfterStart = this.shellWriter;
      if (!writerAfterStart) {
        this.writeTerminal('> Shell is not ready yet. Try + again in a second.', true);
        return;
      }
      writerAfterStart('\r');
      setTimeout(() => this.terminalRef?.focus(), 100);
      return;
    }

    const writer = existingWriter;

    // Reset the current shell session instead of respawning a runtime context.
    writer('\u0003\r');
    this.terminalRef?.clear();
    this.writeTerminal('> New terminal ready. Type your command and press Enter.', true);
    writer('cd /\r');
    writer('\r');
    setTimeout(() => this.terminalRef?.focus(), 100);
  }

  togglePanel(p: Panel): void { this.panel.set(p); }
  toggleBottomPanel(p: BottomPanel): void {
    this.bottomPanel.set(this.bottomPanel() === p ? 'hidden' : p);
  }
  openTemplateSelector(): void {
    this.showTemplateSelector.set(true);
    if (this.templates().length === 0 && !this.templatesLoading()) {
      this.loadTemplates(true);
    }
  }
  closeTemplateSelector(): void { this.showTemplateSelector.set(false); }

  retryTemplates(): void {
    this.loadTemplates(true);
  }

  runStartCommand(): void {
    this.bottomPanel.set('terminal');
    this.runStage.set('starting');
    this.runMessage.set('Starting development server');
    this.startStartWatchdog();
    this.writeTerminal('> Starting dev server...', true);
    const startCommand = '(npm run start -- --host 0.0.0.0 --port 4200 --no-progress || npm start -- --host 0.0.0.0 --port 4200 --no-progress || npm run dev)\r';
    if (!this.shellWriter) {
      void this.startShell().then(() => {
        this.shellWriter?.(startCommand);
      });
      return;
    }
    this.shellWriter(startCommand);
  }

  getTabName(path: string): string { return path.split('/').pop() ?? path; }

  trackByPath(_: number, f: { path: string }): string { return f.path; }

  clearRunLogs(marker?: string): void {
    this.runLogs.set([]);
    this.logChunkBuffer = '';
    if (marker) {
      this.appendRunLog(`> ${marker}`, true);
    }
  }

  async copyRunLogs(): Promise<void> {
    const buffered = this.logChunkBuffer.trim();
    const allLogs = buffered
      ? [...this.runLogs(), buffered]
      : this.runLogs();

    if (allLogs.length === 0) {
      this.writeTerminal('> No logs to copy yet.', true);
      return;
    }

    try {
      await navigator.clipboard.writeText(allLogs.join('\n'));
      this.writeTerminal(`> Copied ${allLogs.length} log lines to clipboard.`, true);
    } catch {
      this.writeTerminal('> Could not access clipboard in this browser. Copy directly from the logs panel.', true);
    }
  }

  private writeTerminal(text: string, line = false): void {
    this.appendRunLog(text, line);
    if (this.terminalRef) {
      this.terminalRef.refresh();
      if (line) {
        this.terminalRef.writeLine(text);
      } else {
        this.terminalRef.write(text);
      }
      return;
    }
    this.pendingTerminalOutput.push({ text, line });
  }

  private appendRunLog(text: string, line: boolean): void {
    const cleaned = this.stripAnsi(text).replace(/\r/g, '');

    if (line) {
      const mergedLine = `${this.logChunkBuffer}${cleaned}`.trim();
      this.logChunkBuffer = '';
      if (mergedLine) {
        this.pushRunLogLines([mergedLine]);
      }
      return;
    }

    const chunks = `${this.logChunkBuffer}${cleaned}`.split('\n');
    this.logChunkBuffer = chunks.pop() ?? '';
    const completeLines = chunks.map((lineText) => lineText.trimEnd()).filter((lineText) => lineText.length > 0);
    if (completeLines.length > 0) {
      this.pushRunLogLines(completeLines);
    }
  }

  private pushRunLogLines(lines: string[]): void {
    this.runLogs.update((current) => {
      const next = [...current, ...lines];
      return next.length > 500 ? next.slice(-500) : next;
    });
  }

  private stripAnsi(value: string): string {
    return value.replace(/\u001B\[[0-9;]*[A-Za-z]/g, '');
  }

  private startStartWatchdog(): void {
    this.clearStartWatchdog();
    this.startWatchdogTimer = setTimeout(() => {
      if (this.runStage() !== 'starting') return;
      this.runStage.set('idle');
      this.runMessage.set('Start command is still running in terminal');
      this.writeTerminal('> Start command is taking longer than expected. Continue from terminal, or press ▶ again.', true);
    }, 25000);
  }

  private clearStartWatchdog(): void {
    if (!this.startWatchdogTimer) return;
    clearTimeout(this.startWatchdogTimer);
    this.startWatchdogTimer = null;
  }

  private async openPreferredWorkspaceFile(): Promise<void> {
    if (this.activeFilePath()) return;

    const candidates = [
      'src/main.ts',
      'src/app/app.component.ts',
      'src/app/app.component.html',
      'project-template-angular/src/main.ts',
      'project-template-angular/src/app/app.component.ts',
      'project-template-angular/src/app/app.component.html',
    ];

    for (const path of candidates) {
      try {
        const content = await this.wc.readFile(path);
        this.openFile(path, content);
        return;
      } catch {
        // Try next candidate.
      }
    }
  }

  private loadTemplates(forceRefresh = false): void {
    this.templatesLoading.set(true);
    this.templatesError.set('');

    const request$ = forceRefresh
      ? this.templatesService.refreshTemplates()
      : this.templatesService.getTemplates();

    request$.subscribe({
      next: (templates) => {
        this.templates.set(templates);
        this.templatesLoading.set(false);
      },
      error: (err) => {
        const msg = err?.message ?? 'Failed to load templates. Ensure API is running on port 3000.';
        this.templates.set([]);
        this.templatesLoading.set(false);
        this.templatesError.set(msg);
      },
    });
  }

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
