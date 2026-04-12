import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, shareReplay } from 'rxjs';
import { environment } from '../../environments/environment';

export interface TemplateInfo {
  id: string;
  name: string;
  description: string;
  framework: 'angular' | 'react' | 'vue' | 'nodejs' | 'nestjs';
  language: 'typescript' | 'javascript';
}

export interface TemplateFile {
  path: string;
  content: string;
}

export interface TemplateDetail extends TemplateInfo {
  files: TemplateFile[];
}

@Injectable({ providedIn: 'root' })
export class ProjectTemplatesService {
  private http = inject(HttpClient);
  private baseUrl = environment.apiUrl;

  private templateList$: Observable<TemplateInfo[]> | null = null;

  getTemplates(): Observable<TemplateInfo[]> {
    if (!this.templateList$) {
      this.templateList$ = this.http
        .get<TemplateInfo[]>(`${this.baseUrl}/templates`)
        .pipe(shareReplay(1));
    }
    return this.templateList$;
  }

  refreshTemplates(): Observable<TemplateInfo[]> {
    this.templateList$ = null;
    return this.getTemplates();
  }

  getTemplate(id: string): Observable<TemplateDetail> {
    return this.http.get<TemplateDetail>(`${this.baseUrl}/templates/${id}`);
  }
}
