import { Module } from '@nestjs/common';
import { DatabaseConfig } from './database.config';
import { DatabaseService } from './database.service';

@Module({
  providers: [DatabaseConfig, DatabaseService],
  exports: [DatabaseService, DatabaseConfig],
})
export class DatabaseModule {}
