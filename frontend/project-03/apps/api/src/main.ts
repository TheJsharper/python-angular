import { Logger, ValidationPipe } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import helmet from 'helmet';
import { AppModule } from './app/app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Security: Helmet + COOP/COEP (required by WebContainers API)
  app.use(
    helmet({
      contentSecurityPolicy: false,
      crossOriginOpenerPolicy: { policy: 'same-origin' },
      crossOriginEmbedderPolicy: { policy: 'require-corp' },
    }),
  );

  app.use((_req: unknown, res: any, next: () => void) => {
    res.setHeader('Cross-Origin-Opener-Policy', 'same-origin');
    res.setHeader('Cross-Origin-Embedder-Policy', 'require-corp');
    next();
  });

  app.enableCors({
    origin: ['http://localhost:4200', 'http://localhost:4201', 'http://localhost:4300'],
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
    credentials: true,
  });

  app.useGlobalPipes(new ValidationPipe({ whitelist: true, transform: true }));
  app.setGlobalPrefix('api');

  const port = process.env.PORT || 3000;
  await app.listen(port);
  Logger.log(`=== API running on: http://localhost:${port}/api`);
}

bootstrap();
