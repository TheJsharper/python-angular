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

  ngAfterViewInit(): void {
    this.terminal = new Terminal({
      cursorBlink: true,
      fontSize: 13,
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
  }

  ngOnDestroy(): void {
    this.resizeObserver?.disconnect();
    this.terminal?.dispose();
  }

  write(data: string): void {
    this.terminal?.write(data);
    this.terminal?.scrollToBottom();
  }

  writeLine(line: string): void {
    this.terminal?.writeln(line);
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
}
