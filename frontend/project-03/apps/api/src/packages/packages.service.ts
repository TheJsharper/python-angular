import { Injectable, BadRequestException } from '@nestjs/common';

export interface PackageInfo {
  name: string;
  version: string;
  description: string;
  keywords: string[];
  homepage: string;
  license: string;
  latestVersion: string;
}

export interface PackageSearchResult {
  name: string;
  version: string;
  description: string;
}

const ALLOWED_PACKAGE_PATTERN = /^(?:@[a-z0-9-~][a-z0-9-._~]*\/)?[a-z0-9-~][a-z0-9-._~]*$/;

@Injectable()
export class PackagesService {
  private readonly registryBase = 'https://registry.npmjs.org';

  private validatePackageName(name: string): void {
    if (!ALLOWED_PACKAGE_PATTERN.test(name)) {
      throw new BadRequestException('Invalid package name');
    }
    if (name.length > 214) {
      throw new BadRequestException('Package name too long');
    }
  }

  async search(query: string): Promise<PackageSearchResult[]> {
    if (!query || query.trim().length === 0) {
      return [];
    }
    const q = encodeURIComponent(query.trim().substring(0, 100));
    const url = `https://registry.npmjs.org/-/v1/search?text=${q}&size=20`;
    const res = await fetch(url, {
      headers: { Accept: 'application/json' },
      signal: AbortSignal.timeout(5000),
    });
    if (!res.ok) {
      throw new BadRequestException(`npm registry error: ${res.status}`);
    }
    const data = await res.json() as { objects: { package: { name: string; version: string; description: string } }[] };
    return data.objects.map((o) => ({
      name: o.package.name,
      version: o.package.version,
      description: o.package.description ?? '',
    }));
  }

  async getPackageInfo(name: string): Promise<PackageInfo> {
    this.validatePackageName(name);
    const url = `${this.registryBase}/${encodeURIComponent(name).replace('%40', '@').replace('%2F', '/')}`;
    const res = await fetch(url, {
      headers: { Accept: 'application/json' },
      signal: AbortSignal.timeout(5000),
    });
    if (!res.ok) {
      throw new BadRequestException(`Package "${name}" not found on npm`);
    }
    const data = await res.json() as {
      name: string;
      description?: string;
      keywords?: string[];
      homepage?: string;
      license?: string;
      'dist-tags': { latest?: string };
      versions: Record<string, { version: string }>;
    };
    const latest = data['dist-tags']?.latest ?? '';
    return {
      name: data.name,
      version: data.versions?.[latest]?.version ?? latest,
      description: data.description ?? '',
      keywords: data.keywords ?? [],
      homepage: data.homepage ?? '',
      license: data.license ?? '',
      latestVersion: latest,
    };
  }
}
