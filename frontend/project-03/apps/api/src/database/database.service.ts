import { Injectable, OnApplicationBootstrap, Logger } from '@nestjs/common';
import { DatabaseConfig } from './database.config';
import { InMemoryProjectRepository } from './in-memory.repository';
import { PostgresProjectRepository } from './postgres.repository';
import { IProjectRepository } from './project.repository.interface';

@Injectable()
export class DatabaseService implements OnApplicationBootstrap {
  private logger = new Logger(DatabaseService.name);
  private repository: IProjectRepository;

  constructor(private config: DatabaseConfig) {}

  async onApplicationBootstrap(): Promise<void> {
    if (this.config.isMemory) {
      this.logger.log('Database: Using in-memory store');
      this.repository = new InMemoryProjectRepository();
    } else if (this.config.isPostgres) {
      this.logger.log(`Database: Connecting to PostgreSQL at ${this.config.host}:${this.config.port}/${this.config.database}`);
      const pgRepository = new PostgresProjectRepository(this.config);
      await pgRepository.initialize();
      this.repository = pgRepository;
      this.logger.log('Database: PostgreSQL connection established');
    } else {
      throw new Error(`Unknown DB_TYPE: ${this.config.dbType}`);
    }
  }

  getRepository(): IProjectRepository {
    if (!this.repository) {
      throw new Error('Database not initialized. Ensure onApplicationBootstrap has been called.');
    }
    return this.repository;
  }
}
