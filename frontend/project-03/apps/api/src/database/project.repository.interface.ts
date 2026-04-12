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

export interface IProjectRepository {
  findAll(): Promise<Project[]>;
  findOne(id: string): Promise<Project | null>;
  create(project: Omit<Project, 'id' | 'createdAt' | 'updatedAt'>): Promise<Project>;
  update(id: string, updates: Partial<Project>): Promise<Project>;
  remove(id: string): Promise<void>;
}
