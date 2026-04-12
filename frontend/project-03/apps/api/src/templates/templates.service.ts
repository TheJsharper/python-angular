import { Injectable, NotFoundException } from '@nestjs/common';

export interface TemplateFile {
  path: string;
  content: string;
}

export interface Template {
  id: string;
  name: string;
  description: string;
  framework: 'angular' | 'react' | 'vue' | 'nodejs' | 'nestjs';
  language: 'typescript' | 'javascript';
  files: TemplateFile[];
}

const TEMPLATES: Template[] = [
  {
    id: 'angular-ts',
    name: 'Angular',
    description: 'Angular CLI-style standalone app scaffold for start-project',
    framework: 'angular',
    language: 'typescript',
    files: [
      {
        path: 'package.json',
        content: JSON.stringify(
          {
            name: 'project',
            version: '0.0.0',
            private: true,
            scripts: {
              ng: 'ng',
              start: 'ng serve --host 0.0.0.0 --port 4200 --no-progress --verbose',
              build: 'ng build',
              watch: 'ng build --watch --configuration development',
              test: 'ng test',
            },
            dependencies: {
              '@angular/animations': '^17.3.0',
              '@angular/common': '^17.3.0',
              '@angular/compiler': '^17.3.0',
              '@angular/core': '^17.3.0',
              '@angular/forms': '^17.3.0',
              '@angular/platform-browser': '^17.3.0',
              '@angular/platform-browser-dynamic': '^17.3.0',
              '@angular/router': '^17.3.0',
              rxjs: '~7.8.0',
              tslib: '^2.3.0',
              'zone.js': '~0.14.3',
            },
            devDependencies: {
              '@angular-devkit/build-angular': '^17.3.17',
              '@angular/cli': '^17.3.17',
              '@angular/compiler-cli': '^17.3.0',
              '@types/jasmine': '~5.1.0',
              'jasmine-core': '~5.1.0',
              karma: '~6.4.0',
              'karma-chrome-launcher': '~3.2.0',
              'karma-coverage': '~2.2.0',
              'karma-jasmine': '~5.1.0',
              'karma-jasmine-html-reporter': '~2.1.0',
              typescript: '~5.4.2',
            },
          },
          null,
          2,
        ),
      },
      {
        path: 'README.md',
        content: `# start-project

Generated with Angular CLI-style scaffold.

## Development server

Run \`npm start\` for a dev server and open http://localhost:4200/.

## Build

Run \`npm run build\` to build the project.
`,
      },
      {
        path: '.editorconfig',
        content: `# Editor configuration
root = true

[*.{ts,js,scss,html}]
indent_style = space
indent_size = 2
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
`,
      },
      {
        path: '.gitignore',
        content: `/node_modules
/dist
/.angular
/.vscode
npm-debug.log*
yarn-debug.log*
yarn-error.log*
`,
      },
      {
        path: '.vscode/extensions.json',
        content: JSON.stringify(
          {
            recommendations: [
              'angular.ng-template',
              'dbaeumer.vscode-eslint',
              'esbenp.prettier-vscode',
            ],
          },
          null,
          2,
        ),
      },
      {
        path: '.vscode/settings.json',
        content: JSON.stringify(
          {
            'typescript.tsdk': 'node_modules/typescript/lib',
            'editor.formatOnSave': true,
            'editor.codeActionsOnSave': {
              'source.fixAll.eslint': 'explicit',
            },
            'files.exclude': {
              '**/.angular': true,
              '**/dist': true,
              '**/node_modules': true,
            },
            'angular.suggest.includeAutomaticOptionalChainCompletions': true,
          },
          null,
          2,
        ),
      },
      {
        path: 'angular.json',
        content: JSON.stringify(
          {
            $schema: './node_modules/@angular/cli/lib/config/schema.json',
            version: 1,
            newProjectRoot: 'projects',
            projects: {
              'start-project': {
                projectType: 'application',
                schematics: {
                  '@schematics/angular:component': {
                    style: 'scss',
                  },
                },
                root: '',
                sourceRoot: 'src',
                prefix: 'app',
                architect: {
                  build: {
                    builder: '@angular-devkit/build-angular:application',
                    options: {
                      outputPath: 'dist/start-project',
                      index: 'src/index.html',
                      browser: 'src/main.ts',
                      polyfills: ['zone.js'],
                      tsConfig: 'tsconfig.app.json',
                      inlineStyleLanguage: 'scss',
                      assets: ['src/favicon.ico', 'src/assets'],
                      styles: ['src/styles.scss'],
                      scripts: [],
                    },
                    configurations: {
                      production: {
                        budgets: [
                          {
                            type: 'initial',
                            maximumWarning: '500kb',
                            maximumError: '1mb',
                          },
                          {
                            type: 'anyComponentStyle',
                            maximumWarning: '2kb',
                            maximumError: '4kb',
                          },
                        ],
                        outputHashing: 'all',
                      },
                      development: {
                        optimization: false,
                        extractLicenses: false,
                        sourceMap: true,
                      },
                    },
                    defaultConfiguration: 'production',
                  },
                  serve: {
                    builder: '@angular-devkit/build-angular:dev-server',
                    configurations: {
                      production: {
                        buildTarget: 'start-project:build:production',
                      },
                      development: {
                        buildTarget: 'start-project:build:development',
                      },
                    },
                    defaultConfiguration: 'development',
                  },
                  'extract-i18n': {
                    builder: '@angular-devkit/build-angular:extract-i18n',
                    options: {
                      buildTarget: 'start-project:build',
                    },
                  },
                  test: {
                    builder: '@angular-devkit/build-angular:karma',
                    options: {
                      polyfills: ['zone.js', 'zone.js/testing'],
                      tsConfig: 'tsconfig.spec.json',
                      inlineStyleLanguage: 'scss',
                      assets: ['src/favicon.ico', 'src/assets'],
                      styles: ['src/styles.scss'],
                      scripts: [],
                    },
                  },
                },
              },
            },
          },
          null,
          2,
        ),
      },
      {
        path: 'tsconfig.json',
        content: JSON.stringify(
          {
            compileOnSave: false,
            compilerOptions: {
              outDir: './dist/out-tsc',
              strict: true,
              noImplicitOverride: true,
              noPropertyAccessFromIndexSignature: true,
              noImplicitReturns: true,
              noFallthroughCasesInSwitch: true,
              skipLibCheck: true,
              esModuleInterop: true,
              sourceMap: true,
              declaration: false,
              experimentalDecorators: true,
              moduleResolution: 'node',
              importHelpers: true,
              target: 'ES2022',
              module: 'ES2022',
              useDefineForClassFields: false,
              lib: ['ES2022', 'dom'],
            },
            angularCompilerOptions: {
              enableI18nLegacyMessageIdFormat: false,
              strictInjectionParameters: true,
              strictInputAccessModifiers: true,
              strictTemplates: true,
            },
          },
          null,
          2,
        ),
      },
      {
        path: 'tsconfig.app.json',
        content: JSON.stringify(
          {
            extends: './tsconfig.json',
            compilerOptions: {
              outDir: './out-tsc/app',
              types: [],
            },
            files: ['src/main.ts'],
            include: ['src/**/*.d.ts'],
          },
          null,
          2,
        ),
      },
      {
        path: 'tsconfig.spec.json',
        content: JSON.stringify(
          {
            extends: './tsconfig.json',
            compilerOptions: {
              outDir: './out-tsc/spec',
              types: ['jasmine'],
            },
            include: ['src/**/*.spec.ts', 'src/**/*.d.ts'],
          },
          null,
          2,
        ),
      },
      {
        path: 'src/index.html',
        content: `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>StartProject</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <app-root></app-root>
</body>
</html>
`,
      },
      {
        path: 'src/main.ts',
        content: `import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));
`,
      },
      {
        path: 'src/styles.scss',
        content: `/* You can add global styles to this file, and also import other style files */
`,
      },
      {
        path: 'src/favicon.ico',
        content: '',
      },
      {
        path: 'src/app/app.component.ts',
        content: `import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'start-project';
}
`,
      },
      {
        path: 'src/app/app.component.spec.ts',
        content: `import { TestBed } from '@angular/core/testing';
import { AppComponent } from './app.component';

describe('AppComponent', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AppComponent],
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(\`should have the 'start-project' title\`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('start-project');
  });

  it('should render title', () => {
    const fixture = TestBed.createComponent(AppComponent);
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h1')?.textContent).toContain('start-project');
  });
});
`,
      },
      {
        path: 'src/app/app.component.html',
        content: `<main>
  <h1>{{ title }}</h1>
  <p>Angular CLI project scaffold is ready.</p>
  <router-outlet></router-outlet>
</main>
`,
      },
      {
        path: 'src/app/app.component.scss',
        content: `main {
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 0.5rem;
  text-align: center;
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
}

h1 {
  margin: 0;
  color: #dd0031;
}
`,
      },
      {
        path: 'src/app/app.config.ts',
        content: `import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes)],
};
`,
      },
      {
        path: 'src/app/app.routes.ts',
        content: `import { Routes } from '@angular/router';

export const routes: Routes = [];
`,
      },
      {
        path: 'src/assets/.gitkeep',
        content: '',
      },
      {
        path: 'src/assets/README.md',
        content: `Place static files here (images, icons, etc.).
`,
      },
    ],
  },
  {
    id: 'react-ts',
    name: 'React + TypeScript',
    description: 'React 18 + Vite + TypeScript starter',
    framework: 'react',
    language: 'typescript',
    files: [
      {
        path: 'package.json',
        content: JSON.stringify(
          {
            name: 'react-playground',
            version: '0.0.0',
            type: 'module',
            scripts: { dev: 'vite', build: 'tsc && vite build', preview: 'vite preview' },
            dependencies: { react: '^18.2.0', 'react-dom': '^18.2.0' },
            devDependencies: {
              '@types/react': '^18.2.0',
              '@types/react-dom': '^18.2.0',
              '@vitejs/plugin-react': '^4.0.0',
              typescript: '^5.0.0',
              vite: '^5.0.0',
            },
          },
          null,
          2,
        ),
      },
      {
        path: 'src/main.tsx',
        content: `import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
`,
      },
      {
        path: 'src/App.tsx',
        content: `import React, { useState } from 'react';

export default function App() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h1>React Playground</h1>
      <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>
    </div>
  );
}
`,
      },
      {
        path: 'index.html',
        content: `<!DOCTYPE html>
<html lang="en">
  <head><meta charset="UTF-8" /><title>React Playground</title></head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
`,
      },
      {
        path: 'vite.config.ts',
        content: `import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
export default defineConfig({ plugins: [react()] });
`,
      },
    ],
  },
  {
    id: 'vue-ts',
    name: 'Vue 3 + TypeScript',
    description: 'Vue 3 + Vite + Composition API starter',
    framework: 'vue',
    language: 'typescript',
    files: [
      {
        path: 'package.json',
        content: JSON.stringify(
          {
            name: 'vue-playground',
            version: '0.0.0',
            type: 'module',
            scripts: { dev: 'vite', build: 'vite build', preview: 'vite preview' },
            dependencies: { vue: '^3.3.0' },
            devDependencies: {
              '@vitejs/plugin-vue': '^4.2.0',
              typescript: '^5.0.0',
              vite: '^5.0.0',
            },
          },
          null,
          2,
        ),
      },
      {
        path: 'src/main.ts',
        content: `import { createApp } from 'vue';
import App from './App.vue';
createApp(App).mount('#app');
`,
      },
      {
        path: 'src/App.vue',
        content: `<script setup lang="ts">
import { ref } from 'vue';
const count = ref(0);
</script>

<template>
  <h1>Vue Playground</h1>
  <button @click="count++">Count: {{ count }}</button>
</template>
`,
      },
      {
        path: 'index.html',
        content: `<!DOCTYPE html>
<html lang="en">
  <head><meta charset="UTF-8" /><title>Vue Playground</title></head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>
`,
      },
      {
        path: 'vite.config.ts',
        content: `import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
export default defineConfig({ plugins: [vue()] });
`,
      },
    ],
  },
  {
    id: 'nodejs-ts',
    name: 'Node.js + TypeScript',
    description: 'Express + TypeScript server starter',
    framework: 'nodejs',
    language: 'typescript',
    files: [
      {
        path: 'package.json',
        content: JSON.stringify(
          {
            name: 'node-playground',
            version: '0.0.0',
            scripts: { start: 'ts-node src/index.ts', dev: 'ts-node-dev src/index.ts' },
            dependencies: { express: '^4.18.0' },
            devDependencies: {
              '@types/express': '^4.17.0',
              '@types/node': '^20.0.0',
              'ts-node': '^10.9.0',
              'ts-node-dev': '^2.0.0',
              typescript: '^5.0.0',
            },
          },
          null,
          2,
        ),
      },
      {
        path: 'src/index.ts',
        content: `import express, { Request, Response } from 'express';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (_req: Request, res: Response) => {
  res.json({ message: 'Hello from Node.js Playground!' });
});

app.listen(PORT, () => {
  console.log(\`Server running on http://localhost:\${PORT}\`);
});
`,
      },
      {
        path: 'tsconfig.json',
        content: JSON.stringify(
          {
            compilerOptions: {
              target: 'ES2020',
              module: 'commonjs',
              strict: true,
              esModuleInterop: true,
              outDir: './dist',
            },
          },
          null,
          2,
        ),
      },
    ],
  },
  {
    id: 'nestjs-ts',
    name: 'NestJS',
    description: 'NestJS REST API starter',
    framework: 'nestjs',
    language: 'typescript',
    files: [
      {
        path: 'package.json',
        content: JSON.stringify(
          {
            name: 'nestjs-playground',
            version: '0.0.0',
            scripts: { start: 'nest start', dev: 'nest start --watch', build: 'nest build' },
            dependencies: {
              '@nestjs/common': '^11.0.0',
              '@nestjs/core': '^11.0.0',
              '@nestjs/platform-express': '^11.0.0',
              'reflect-metadata': '^0.1.13',
              rxjs: '~7.8.0',
            },
            devDependencies: {
              '@nestjs/cli': '^10.0.0',
              '@nestjs/schematics': '^10.0.0',
              typescript: '^5.0.0',
            },
          },
          null,
          2,
        ),
      },
      {
        path: 'src/main.ts',
        content: `import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
`,
      },
      {
        path: 'src/app.module.ts',
        content: `import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
`,
      },
      {
        path: 'src/app.controller.ts',
        content: `import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}
`,
      },
      {
        path: 'src/app.service.ts',
        content: `import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World from NestJS Playground!';
  }
}
`,
      },
    ],
  },
];

@Injectable()
export class TemplatesService {
  findAll(): Omit<Template, 'files'>[] {
    return TEMPLATES.map((template) => ({
      id: template.id,
      name: template.name,
      description: template.description,
      framework: template.framework,
      language: template.language,
    }));
  }

  findOne(id: string): Template {
    const template = TEMPLATES.find((t) => t.id === id);
    if (!template) {
      throw new NotFoundException(`Template "${id}" not found`);
    }
    return template;
  }
}
