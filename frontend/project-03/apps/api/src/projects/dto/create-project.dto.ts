export class CreateProjectDto {
  name!: string;
  template!: string;
  files?: { path: string; content: string }[];
}
