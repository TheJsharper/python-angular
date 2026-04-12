import {
  Component,
  ElementRef,
  Input,
  Output,
  EventEmitter,
  AfterViewInit,
  OnDestroy,
  ViewChild,
} from '@angular/core';
import { Terminal } from '@xterm/xterm';
import { FitAddon } from '@xterm/addon-fit';
import { WebLinksAddon } from '@xterm/addon-web-links';

@Component({
  selector: 'app-terminal',
  standalone: true,
  template: `<div #terminalContainer class="terminal-container"></div>`,
  styles: [`
    :host { display: flex; flex-direction: column; flex: 1; overflow: hidden; background: #1e1e1e; }
    .terminal-container { flex: 1; padding: 4px; overflow: hidden; }
  `],
})
export class TerminalComponent implements AfterViewInit, OnDestroy {
  @ViewChild('terminalContainer', { static: true }) container!: ElementRef<HTMLDivElement>;

  @Output() data = new EventEmitter<string>();

  private terminal: Terminal | null = null;
  private fitAddon: FitAddon | null = null;
  private resizeObserver: ResizeObserver | null = null;
  private pendingWrites: Array<{ text: string; line: boolean }> = [];

  ngAfterViewInit(): void {
    this.terminal = new Terminal({
      cursorBlink: true,
      fontSize: 13,
      scrollback: 10000,
      convertEol: true,
      fontFamily: "'Cascadia Code', 'Fira Code', 'Consolas', monospace",
      theme: {
        background: '#1e1e1e',
        foreground: '#d4d4d4',
        cursor: '#d4d4d4',
        black: '#1e1e1e',
        brightBlack: '#555555',
        red: '#cd3131',
        brightRed: '#f14c4c',
        green: '#0dbc79',
        brightGreen: '#23d18b',
        yellow: '#e5e510',
        brightYellow: '#f5f543',
        blue: '#2472c8',
        brightBlue: '#3b8eea',
        magenta: '#bc3fbc',
        brightMagenta: '#d670d6',
        cyan: '#11a8cd',
        brightCyan: '#29b8db',
        white: '#e5e5e5',
        brightWhite: '#e5e5e5',
      },
    });

    this.fitAddon = new FitAddon();
    this.terminal.loadAddon(this.fitAddon);
    this.terminal.loadAddon(new WebLinksAddon());
    this.terminal.open(this.container.nativeElement);
    this.fitAddon.fit();

    this.terminal.onData((d) => this.data.emit(d));

    this.resizeObserver = new ResizeObserver(() => {
      this.fitAddon?.fit();
    });
    this.resizeObserver.observe(this.container.nativeElement);

    if (this.pendingWrites.length > 0) {
      const queued = [...this.pendingWrites];
      this.pendingWrites = [];
      for (const entry of queued) {
        if (entry.line) {
          this.terminal.writeln(this.normalizeOutput(entry.text));
        } else {
          this.terminal.write(this.normalizeOutput(entry.text));
        }
      }
      this.terminal.scrollToBottom();
    }
  }

  ngOnDestroy(): void {
    this.resizeObserver?.disconnect();
    this.terminal?.dispose();
  }

  write(data: string): void {
    if (!this.terminal) {
      this.pendingWrites.push({ text: data, line: false });
      return;
    }
    this.terminal?.write(this.normalizeOutput(data));
    this.terminal?.scrollToBottom();
  }

  writeLine(line: string): void {
    if (!this.terminal) {
      this.pendingWrites.push({ text: line, line: true });
      return;
    }
    this.terminal?.writeln(this.normalizeOutput(line));
    this.terminal?.scrollToBottom();
  }

  clear(): void {
    this.terminal?.clear();
  }

  getDimensions(): { cols: number; rows: number } {
    return {
      cols: this.terminal?.cols ?? 80,
      rows: this.terminal?.rows ?? 24,
    };
  }

  focus(): void {
    this.terminal?.focus();
  }

  refresh(): void {
    if (!this.terminal) return;
    requestAnimationFrame(() => this.fitAddon?.fit());
    setTimeout(() => this.fitAddon?.fit(), 0);
  }

  private normalizeOutput(data: string): string {
    // Strip ANSI control/color sequences so logs stay readable and visible.
    return data
      .replace(/\x1B\[[0-?]*[ -/]*[@-~]/g, '')
      .replace(/\x1B\][^\x07]*(\x07|\x1B\\)/g, '')
      .replace(/\x1B[P^_][\s\S]*?\x1B\\/g, '')
      .replace(/\r(?!\n)/g, '\n');
  }
}
