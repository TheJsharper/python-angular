import { Injectable, NotFoundException } from '@nestjs/common';
import { DatabaseService } from '../database/database.service';
import { Project } from '../database/project.repository.interface';
import { CreateProjectDto } from './dto/create-project.dto';
import { UpdateProjectDto } from './dto/update-project.dto';

@Injectable()
export class ProjectsService {
  constructor(private databaseService: DatabaseService) {}

  async findAll(): Promise<Project[]> {
    return this.databaseService.getRepository().findAll();
  }

  async findOne(id: string): Promise<Project> {
    const project = await this.databaseService.getRepository().findOne(id);
    if (!project) {
      throw new NotFoundException(`Project ${id} not found`);
    }
    return project;
  }

  async create(dto: CreateProjectDto): Promise<Project> {
    return this.databaseService.getRepository().create({
      name: dto.name,
      template: dto.template,
      files: dto.files ?? [],
    });
  }

  async update(id: string, dto: UpdateProjectDto): Promise<Project> {
    const existing = await this.findOne(id);
    return this.databaseService.getRepository().update(id, {
      ...existing,
      ...dto,
    });
  }

  async remove(id: string): Promise<void> {
    return this.databaseService.getRepository().remove(id);
  }
}
