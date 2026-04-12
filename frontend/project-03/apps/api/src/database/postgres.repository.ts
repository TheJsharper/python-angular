import { Injectable, NotFoundException, OnApplicationShutdown } from '@nestjs/common';
import { DataSource, Repository } from 'typeorm';
import { randomUUID } from 'crypto';
import { IProjectRepository, Project } from './project.repository.interface';
import { ProjectEntity } from './project.entity';
import { DatabaseConfig } from './database.config';

@Injectable()
export class PostgresProjectRepository implements IProjectRepository, OnApplicationShutdown {
  private dataSource: DataSource;
  private repository: Repository<ProjectEntity>;

  constructor(private config: DatabaseConfig) {}

  async initialize(): Promise<void> {
    this.dataSource = new DataSource({
      type: 'postgres',
      url: this.config.connectionString,
      entities: [ProjectEntity],
      synchronize: true, // Auto-migrate in dev; use migrations in prod
      logging: process.env.LOG_LEVEL === 'debug',
    });

    await this.dataSource.initialize();
    this.repository = this.dataSource.getRepository(ProjectEntity);
  }

  async findAll(): Promise<Project[]> {
    const entities = await this.repository.find();
    return entities.map((e) => e.toProject());
  }

  async findOne(id: string): Promise<Project | null> {
    const entity = await this.repository.findOne({ where: { id } });
    return entity ? entity.toProject() : null;
  }

  async create(data: Omit<Project, 'id' | 'createdAt' | 'updatedAt'>): Promise<Project> {
    const entity = this.repository.create({
      id: randomUUID(),
      name: data.name,
      template: data.template,
      files: data.files ?? [],
    });
    await this.repository.save(entity);
    return entity.toProject();
  }

  async update(id: string, updates: Partial<Project>): Promise<Project> {
    const existing = await this.repository.findOne({ where: { id } });
    if (!existing) {
      throw new NotFoundException(`Project ${id} not found`);
    }
    Object.assign(existing, updates);
    await this.repository.save(existing);
    return existing.toProject();
  }

  async remove(id: string): Promise<void> {
    const result = await this.repository.delete(id);
    if (result.affected === 0) {
      throw new NotFoundException(`Project ${id} not found`);
    }
  }

  async onApplicationShutdown(): Promise<void> {
    if (this.dataSource?.isInitialized) {
      await this.dataSource.destroy();
    }
  }
}
