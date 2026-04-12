import { Component, Input, ChangeDetectionStrategy } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-preview',
  standalone: true,
  imports: [CommonModule],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="preview-shell">
      <div class="preview-toolbar">
        <span class="preview-toolbar__label">Preview</span>
        <span class="preview-toolbar__url" *ngIf="url">{{ url }}</span>
        <button class="icon-btn" title="Refresh" *ngIf="url" (click)="refreshFrame()">⟳</button>
        <button class="icon-btn" title="Open in new tab" *ngIf="url" (click)="openInTab()">⤢</button>
      </div>
      <div class="preview-body">
        <ng-container *ngIf="url; else noPreview">
          <iframe
            #frame
            class="preview-frame"
            [src]="sanitizedUrl"
            sandbox="allow-scripts allow-same-origin allow-forms allow-modals allow-popups"
            allow="cross-origin-isolated"
          ></iframe>
        </ng-container>
        <ng-template #noPreview>
          <div class="preview-empty">
            <div class="preview-empty__icon">⚡</div>
            <p>Start your project to see a live preview</p>
          </div>
        </ng-template>
      </div>
    </div>
  `,
  styles: [`
    :host { display: flex; flex-direction: column; flex: 1; overflow: hidden; background: #1e1e1e; }
    .preview-shell { display: flex; flex-direction: column; flex: 1; overflow: hidden; }
    .preview-toolbar { display: flex; align-items: center; gap: 8px; padding: 6px 12px; background: #2d2d2d; border-bottom: 1px solid #3e3e3e; font-size: 12px; color: #cccccc; flex-shrink: 0; }
    .preview-toolbar__label { font-weight: 600; text-transform: uppercase; font-size: 11px; letter-spacing: 0.5px; }
    .preview-toolbar__url { flex: 1; background: #1e1e1e; border-radius: 4px; padding: 2px 8px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: #9cdcfe; }
    .preview-body { flex: 1; overflow: hidden; }
    .preview-frame { width: 100%; height: 100%; border: none; background: #fff; }
    .preview-empty { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; color: #555; gap: 12px; }
    .preview-empty__icon { font-size: 48px; }
    .preview-empty p { font-size: 14px; }
    .icon-btn { background: none; border: none; cursor: pointer; color: #cccccc; padding: 2px 6px; border-radius: 3px; font-size: 14px; }
    .icon-btn:hover { background: rgba(255,255,255,0.1); }
  `],
})
export class PreviewComponent {
  @Input() url = '';

  get sanitizedUrl(): string {
    if (!this.url) return '';
    try {
      const parsed = new URL(this.url.trim());
      return parsed.protocol === 'http:' || parsed.protocol === 'https:' ? parsed.href : '';
    } catch {
      return '';
    }
  }

  refreshFrame(): void {
    const frame = document.querySelector<HTMLIFrameElement>('.preview-frame');
    if (frame) {
      frame.src = frame.src;
    }
  }

  openInTab(): void {
    if (this.sanitizedUrl) {
      window.open(this.sanitizedUrl, '_blank', 'noopener,noreferrer');
    }
  }
}
