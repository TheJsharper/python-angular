import { Entity, PrimaryColumn, Column, CreateDateColumn, UpdateDateColumn, DataSource } from 'typeorm';
import { Project, ProjectFile } from './project.repository.interface';

@Entity('projects')
export class ProjectEntity {
  @PrimaryColumn('uuid')
  id: string;

  @Column()
  name: string;

  @Column()
  template: string;

  @Column('jsonb', { default: '[]' })
  files: ProjectFile[];

  @CreateDateColumn()
  createdAt: Date;

  @UpdateDateColumn()
  updatedAt: Date;

  toProject(): Project {
    return {
      id: this.id,
      name: this.name,
      template: this.template,
      files: this.files,
      createdAt: this.createdAt.toISOString(),
      updatedAt: this.updatedAt.toISOString(),
    };
  }
}
