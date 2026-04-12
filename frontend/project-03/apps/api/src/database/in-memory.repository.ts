import { Injectable, NotFoundException } from '@nestjs/common';
import { randomUUID } from 'crypto';
import { IProjectRepository, Project, ProjectFile } from './project.repository.interface';

@Injectable()
export class InMemoryProjectRepository implements IProjectRepository {
  private store = new Map<string, Project>();

  async findAll(): Promise<Project[]> {
    return Array.from(this.store.values());
  }

  async findOne(id: string): Promise<Project | null> {
    return this.store.get(id) ?? null;
  }

  async create(data: Omit<Project, 'id' | 'createdAt' | 'updatedAt'>): Promise<Project> {
    const now = new Date().toISOString();
    const project: Project = {
      id: randomUUID(),
      name: data.name,
      template: data.template,
      files: data.files ?? [],
      createdAt: now,
      updatedAt: now,
    };
    this.store.set(project.id, project);
    return project;
  }

  async update(id: string, updates: Partial<Project>): Promise<Project> {
    const existing = await this.findOne(id);
    if (!existing) {
      throw new NotFoundException(`Project ${id} not found`);
    }
    const updated: Project = {
      ...existing,
      ...updates,
      id: existing.id,
      createdAt: existing.createdAt,
      updatedAt: new Date().toISOString(),
    };
    this.store.set(id, updated);
    return updated;
  }

  async remove(id: string): Promise<void> {
    if (!this.store.has(id)) {
      throw new NotFoundException(`Project ${id} not found`);
    }
    this.store.delete(id);
  }
}
