import { Component, Input, Output, EventEmitter, ChangeDetectionStrategy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FileNode } from '../../services/web-container.service';

@Component({
  selector: 'app-file-tree',
  standalone: true,
  imports: [CommonModule],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="file-tree">
      <div class="file-tree__header">
        <span>EXPLORER</span>
        <div class="file-tree__actions">
          <button class="icon-btn" title="New File" (click)="onNewFile()">+</button>
          <button class="icon-btn" title="Refresh" (click)="refreshed.emit()">⟳</button>
        </div>
      </div>
      <div class="file-tree__body">
        <ng-container *ngFor="let node of nodes">
          <ng-container *ngTemplateOutlet="nodeTemplate; context: { $implicit: node, depth: 0 }"></ng-container>
        </ng-container>
      </div>
    </div>

    <ng-template #nodeTemplate let-node let-depth="depth">
      <div
        class="tree-item"
        [class.tree-item--selected]="selectedPath === node.path"
        [class.tree-item--file]="node.type === 'file'"
        [class.tree-item--dir]="node.type === 'directory'"
        [style.padding-left.px]="12 + depth * 16"
        (click)="onNodeClick(node)"
      >
        <span class="tree-item__icon">
          {{ node.type === 'directory' ? (expandedDirs.has(node.path) ? '▾' : '▸') : getFileIcon(node.name) }}
        </span>
        <span class="tree-item__name">{{ node.name }}</span>
        <button
          class="icon-btn tree-item__delete"
          title="Delete"
          (click)="onDelete($event, node.path)"
        >×</button>
      </div>
      <ng-container *ngIf="node.type === 'directory' && expandedDirs.has(node.path)">
        <ng-container *ngFor="let child of node.children">
          <ng-container *ngTemplateOutlet="nodeTemplate; context: { $implicit: child, depth: depth + 1 }"></ng-container>
        </ng-container>
      </ng-container>
    </ng-template>
  `,
  styles: [`
    :host { display: flex; flex-direction: column; overflow: hidden; }
    .file-tree { display: flex; flex-direction: column; flex: 1; overflow: hidden; background: #252526; color: #cccccc; font-size: 13px; }
    .file-tree__header { display: flex; justify-content: space-between; align-items: center; padding: 6px 12px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; color: #bbbbbb; }
    .file-tree__actions { display: flex; gap: 4px; }
    .file-tree__body { flex: 1; overflow-y: auto; }
    .tree-item { display: flex; align-items: center; gap: 4px; height: 22px; cursor: pointer; user-select: none; position: relative; }
    .tree-item:hover { background: rgba(255,255,255,0.07); }
    .tree-item--selected { background: #094771 !important; }
    .tree-item__icon { width: 16px; text-align: center; flex-shrink: 0; font-size: 11px; }
    .tree-item__name { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .tree-item__delete { opacity: 0; color: #f48771; background: none; border: none; cursor: pointer; padding: 0 2px; }
    .tree-item:hover .tree-item__delete { opacity: 1; }
    .icon-btn { background: none; border: none; cursor: pointer; color: #cccccc; padding: 2px 4px; border-radius: 3px; font-size: 14px; }
    .icon-btn:hover { background: rgba(255,255,255,0.1); }
  `],
})
export class FileTreeComponent {
  @Input() nodes: FileNode[] = [];
  @Input() selectedPath = '';
  @Output() fileSelected = new EventEmitter<string>();
  @Output() fileDeleted = new EventEmitter<string>();
  @Output() newFileRequested = new EventEmitter<void>();
  @Output() refreshed = new EventEmitter<void>();

  expandedDirs = new Set<string>();

  onNodeClick(node: FileNode): void {
    if (node.type === 'directory') {
      if (this.expandedDirs.has(node.path)) {
        this.expandedDirs.delete(node.path);
      } else {
        this.expandedDirs.add(node.path);
      }
    } else {
      this.fileSelected.emit(node.path);
    }
  }

  onDelete(event: MouseEvent, path: string): void {
    event.stopPropagation();
    this.fileDeleted.emit(path);
  }

  onNewFile(): void {
    this.newFileRequested.emit();
  }

  getFileIcon(name: string): string {
    const ext = name.split('.').pop()?.toLowerCase() ?? '';
    const icons: Record<string, string> = {
      ts: '📄', tsx: '📄', js: '📄', jsx: '📄',
      html: '🌐', css: '🎨', scss: '🎨',
      json: '{}', md: '📝', vue: '💚',
      svg: '🖼', png: '🖼', jpg: '🖼',
    };
    return icons[ext] ?? '📄';
  }
}
