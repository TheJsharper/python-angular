import { Injectable } from '@nestjs/common';

@Injectable()
export class DatabaseConfig {
  readonly dbType: 'memory' | 'postgres' = (process.env.DB_TYPE as 'memory' | 'postgres') || 'memory';
  readonly host: string = process.env.DB_HOST || 'localhost';
  readonly port: number = parseInt(process.env.DB_PORT || '5432', 10);
  readonly database: string = process.env.DB_DATABASE || 'project03_dev';
  readonly username: string = process.env.DB_USERNAME || 'postgres';
  readonly password: string = process.env.DB_PASSWORD || 'postgres';
  readonly databaseUrl: string = process.env.DATABASE_URL || '';

  get connectionString(): string {
    if (this.databaseUrl) return this.databaseUrl;
    return `postgresql://${this.username}:${this.password}@${this.host}:${this.port}/${this.database}`;
  }

  get isMemory(): boolean {
    return this.dbType === 'memory';
  }

  get isPostgres(): boolean {
    return this.dbType === 'postgres';
  }
}
