import { Controller, Get, Param, Query, BadRequestException } from '@nestjs/common';
import { PackagesService } from './packages.service';

@Controller('packages')
export class PackagesController {
  constructor(private readonly packagesService: PackagesService) {}

  @Get('search')
  search(@Query('q') q: string) {
    if (!q) throw new BadRequestException('Query param "q" is required');
    return this.packagesService.search(q);
  }

  @Get(':name')
  findOne(@Param('name') name: string) {
    return this.packagesService.getPackageInfo(name);
  }
}
