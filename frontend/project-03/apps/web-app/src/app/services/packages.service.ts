import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

export interface PackageSearchResult {
  name: string;
  version: string;
  description: string;
}

export interface PackageInfo extends PackageSearchResult {
  keywords: string[];
  homepage: string;
  license: string;
  latestVersion: string;
}

@Injectable({ providedIn: 'root' })
export class PackagesService {
  private http = inject(HttpClient);
  private baseUrl = environment.apiUrl;

  search(query: string): Observable<PackageSearchResult[]> {
    const params = new HttpParams().set('q', query);
    return this.http.get<PackageSearchResult[]>(`${this.baseUrl}/packages/search`, { params });
  }

  getInfo(name: string): Observable<PackageInfo> {
    return this.http.get<PackageInfo>(`${this.baseUrl}/packages/${encodeURIComponent(name)}`);
  }
}
