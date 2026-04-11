import { Injectable, signal } from '@angular/core';
import { WebContainer, WebContainerProcess } from '@webcontainer/api';
import { BehaviorSubject, Subject } from 'rxjs';

export type BootStatus = 'idle' | 'booting' | 'ready' | 'error';

export interface FileNode {
  path: string;
  name: string;
  type: 'file' | 'directory';
  children?: FileNode[];
}

export interface WorkspaceFile {
  path: string;
  content: string;
}

@Injectable({ providedIn: 'root' })
export class WebContainerService {
  private instance: WebContainer | null = null;
  private shellProcess: WebContainerProcess | null = null;

  readonly bootStatus = signal<BootStatus>('idle');
  readonly previewUrl = signal<string>('');
  readonly terminalOutput$ = new Subject<string>();
  readonly fileTree$ = new BehaviorSubject<FileNode[]>([]);

  async boot(): Promise<void> {
    if (this.instance) return;
    this.bootStatus.set('booting');
    try {
      this.instance = await WebContainer.boot();
      this.instance.on('server-ready', (_port, url) => {
        this.previewUrl.set(url);
      });
      this.bootStatus.set('ready');
    } catch (err) {
      this.bootStatus.set('error');
      throw err;
    }
  }

  async mountFiles(files: Record<string, { file: { contents: string } } | { directory: Record<string, unknown> }>): Promise<void> {
    if (!this.instance) throw new Error('WebContainer not booted');
    await this.instance.mount(files as Parameters<WebContainer['mount']>[0]);
    await this.refreshFileTree();
  }

  async loadTemplateFiles(files: WorkspaceFile[]): Promise<void> {
    if (!this.instance) throw new Error('WebContainer not booted');

    await this.clearWorkspace();

    for (const file of files) {
      const normalizedPath = file.path.replace(/^\/+/, '');
      const segments = normalizedPath.split('/');
      const fileName = segments.pop();
      if (!fileName) continue;

      let currentDir = '';
      for (const segment of segments) {
        currentDir = currentDir ? `${currentDir}/${segment}` : segment;
        await this.instance.fs.mkdir(currentDir).catch(() => undefined);
      }

      const fullPath = segments.length > 0 ? `${segments.join('/')}/${fileName}` : fileName;
      await this.instance.fs.writeFile(fullPath, file.content);
    }

    await this.refreshFileTree();
  }

  async writeFile(path: string, content: string): Promise<void> {
    if (!this.instance) throw new Error('WebContainer not booted');
    await this.instance.fs.writeFile(path, content);
    await this.refreshFileTree();
  }

  async readFile(path: string): Promise<string> {
    if (!this.instance) throw new Error('WebContainer not booted');
    return this.instance.fs.readFile(path, 'utf-8');
  }

  async deleteFile(path: string): Promise<void> {
    if (!this.instance) throw new Error('WebContainer not booted');
    await this.instance.fs.rm(path, { recursive: true });
    await this.refreshFileTree();
  }

  async refreshFileTree(): Promise<void> {
    if (!this.instance) return;
    const tree = await this.buildFileTree('');
    this.fileTree$.next(tree);
  }

  private async clearWorkspace(): Promise<void> {
    if (!this.instance) return;
    let entries: string[] = [];
    try {
      entries = await this.instance.fs.readdir('/');
    } catch {
      return;
    }

    for (const entry of entries) {
      if (entry.startsWith('.')) continue;
      await this.instance.fs.rm(entry, { recursive: true }).catch(() => undefined);
    }
  }

  private async buildFileTree(dir: string): Promise<FileNode[]> {
    if (!this.instance) return [];
    const basePath = dir || '/';
    let entries: string[];
    try {
      entries = await this.instance.fs.readdir(basePath);
    } catch {
      return [];
    }
    const nodes: FileNode[] = [];
    for (const name of entries) {
      if (name === 'node_modules' || name.startsWith('.')) continue;
      const fullPath = dir ? `${dir}/${name}` : name;
      try {
        await this.instance.fs.readdir(fullPath);
        const children = await this.buildFileTree(fullPath);
        nodes.push({ path: fullPath, name, type: 'directory', children });
      } catch {
        nodes.push({ path: fullPath, name, type: 'file' });
      }
    }
    return nodes.sort((a, b) => {
      if (a.type !== b.type) return a.type === 'directory' ? -1 : 1;
      return a.name.localeCompare(b.name);
    });
  }

  async spawnShell(
    writeToTerminal: (data: string) => void,
    _resize: (cols: number, rows: number) => void,
  ): Promise<{ write: (data: string) => void; resize: (cols: number, rows: number) => void; kill: () => void }> {
    if (!this.instance) throw new Error('WebContainer not booted');
    const process = await this.instance.spawn('jsh', { terminal: { cols: 80, rows: 24 } });
    this.shellProcess = process;

    process.output.pipeTo(
      new WritableStream({ write(chunk) { writeToTerminal(chunk); } }),
    );

    const input = process.input.getWriter();
    return {
      write: (data: string) => input.write(data),
      resize: (cols: number, rows: number) => process.resize({ cols, rows }),
      kill: () => { process.kill(); this.shellProcess = null; },
    };
  }

  async runCommand(command: string, args: string[]): Promise<number> {
    if (!this.instance) throw new Error('WebContainer not booted');
    const proc = await this.instance.spawn(command, args);
    proc.output.pipeTo(
      new WritableStream({ write: (chunk) => this.terminalOutput$.next(chunk) }),
    );
    return proc.exit;
  }

  async teardown(): Promise<void> {
    if (this.shellProcess) {
      this.shellProcess.kill();
      this.shellProcess = null;
    }
    if (this.instance) {
      this.instance.teardown();
      this.instance = null;
    }
    this.bootStatus.set('idle');
    this.previewUrl.set('');
  }

  isReady(): boolean {
    return this.bootStatus() === 'ready';
  }
}
