import {
  Component,
  ElementRef,
  Input,
  Output,
  EventEmitter,
  OnChanges,
  OnDestroy,
  SimpleChanges,
  ViewChild,
  AfterViewInit,
} from '@angular/core';

type MonacoEditor = import('monaco-editor').editor.IStandaloneCodeEditor;
type Monaco = typeof import('monaco-editor');

@Component({
  selector: 'app-editor',
  standalone: true,
  template: `<div #editorContainer class="editor-container"></div>`,
  styles: [`
    :host { display: flex; flex-direction: column; flex: 1; overflow: hidden; }
    .editor-container { flex: 1; overflow: hidden; }
  `],
})
export class EditorComponent implements AfterViewInit, OnChanges, OnDestroy {
  @ViewChild('editorContainer', { static: true }) container!: ElementRef<HTMLDivElement>;

  @Input() language = 'typescript';
  @Input() value = '';
  @Input() theme: 'vs-dark' | 'vs' | 'hc-black' = 'vs-dark';
  @Input() readOnly = false;
  @Output() valueChange = new EventEmitter<string>();

  private editor: MonacoEditor | null = null;
  private monacoInstance: Monaco | null = null;
  private resizeObserver: ResizeObserver | null = null;
  private suppressChangeEvent = false;
  private win = window as unknown as Record<string, unknown>;

  async ngAfterViewInit(): Promise<void> {
    await this.loadMonaco();
    this.createEditor();
    this.setupResizeObserver();
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (!this.editor) return;

    if (changes['value'] && changes['value'].currentValue !== this.getCurrentValue()) {
      this.suppressChangeEvent = true;
      this.editor.setValue(changes['value'].currentValue ?? '');
      this.suppressChangeEvent = false;
    }

    if (changes['language']) {
      const model = this.editor.getModel();
      if (model && this.monacoInstance) {
        this.monacoInstance.editor.setModelLanguage(model, this.language);
      }
    }

    if (changes['theme'] && this.monacoInstance) {
      this.monacoInstance.editor.setTheme(this.theme);
    }

    if (changes['readOnly']) {
      this.editor.updateOptions({ readOnly: this.readOnly });
    }
  }

  ngOnDestroy(): void {
    this.resizeObserver?.disconnect();
    this.editor?.dispose();
  }

  private async loadMonaco(): Promise<void> {
    if (this.win['monaco']) {
      this.monacoInstance = this.win['monaco'] as Monaco;
      return;
    }
    return new Promise<void>((resolve, reject) => {
      const script = document.createElement('script');
      script.src = 'https://cdn.jsdelivr.net/npm/monaco-editor@0.52.0/min/vs/loader.js';
      script.onload = () => {
        const require = this.win['require'] as {
          config: (opts: Record<string, unknown>) => void;
          (modules: string[], cb: (m: Monaco) => void): void;
        };
        require.config({ paths: { vs: 'https://cdn.jsdelivr.net/npm/monaco-editor@0.52.0/min/vs' } });
        require(['vs/editor/editor.main'], (m: Monaco) => {
          this.monacoInstance = m;
          this.win['monaco'] = m;
          resolve();
        });
      };
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }

  private createEditor(): void {
    if (!this.monacoInstance) return;
    this.editor = this.monacoInstance.editor.create(this.container.nativeElement, {
      value: this.value,
      language: this.language,
      theme: this.theme,
      automaticLayout: false,
      fontSize: 14,
      fontFamily: "'Cascadia Code', 'Fira Code', 'Consolas', monospace",
      fontLigatures: true,
      minimap: { enabled: true },
      scrollBeyondLastLine: false,
      wordWrap: 'on',
      tabSize: 2,
      insertSpaces: true,
      readOnly: this.readOnly,
      renderWhitespace: 'selection',
      smoothScrolling: true,
      cursorBlinking: 'smooth',
      bracketPairColorization: { enabled: true },
    });

    this.editor.onDidChangeModelContent(() => {
      if (!this.suppressChangeEvent) {
        this.valueChange.emit(this.getCurrentValue());
      }
    });
  }

  private setupResizeObserver(): void {
    this.resizeObserver = new ResizeObserver(() => {
      this.editor?.layout();
    });
    this.resizeObserver.observe(this.container.nativeElement);
  }

  private getCurrentValue(): string {
    return this.editor?.getValue() ?? '';
  }

  focus(): void {
    this.editor?.focus();
  }

  formatDocument(): void {
    this.editor?.getAction('editor.action.formatDocument')?.run();
  }
}
