import { Injectable, NotFoundException } from '@nestjs/common';
import { randomUUID } from 'crypto';
import { CreateProjectDto } from './dto/create-project.dto';
import { UpdateProjectDto } from './dto/update-project.dto';

export interface ProjectFile {
  path: string;
  content: string;
}

export interface Project {
  id: string;
  name: string;
  template: string;
  files: ProjectFile[];
  createdAt: string;
  updatedAt: string;
}

// In-memory store — replace with database in production
const store = new Map<string, Project>();

@Injectable()
export class ProjectsService {
  findAll(): Project[] {
    return Array.from(store.values());
  }

  findOne(id: string): Project {
    const project = store.get(id);
    if (!project) {
      throw new NotFoundException(`Project ${id} not found`);
    }
    return project;
  }

  create(dto: CreateProjectDto): Project {
    const now = new Date().toISOString();
    const project: Project = {
      id: randomUUID(),
      name: dto.name,
      template: dto.template,
      files: dto.files ?? [],
      createdAt: now,
      updatedAt: now,
    };
    store.set(project.id, project);
    return project;
  }

  update(id: string, dto: UpdateProjectDto): Project {
    const project = this.findOne(id);
    const updated: Project = {
      ...project,
      ...dto,
      updatedAt: new Date().toISOString(),
    };
    store.set(id, updated);
    return updated;
  }

  remove(id: string): void {
    if (!store.has(id)) {
      throw new NotFoundException(`Project ${id} not found`);
    }
    store.delete(id);
  }
}
