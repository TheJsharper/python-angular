export class UpdateProjectDto {
  name?: string;
  files?: { path: string; content: string }[];
}
