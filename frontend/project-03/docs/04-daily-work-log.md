# Project-03 Daily Work Log

## 2026-04-12
### Completed
- [T-2026-04-12-005] Created project docs baseline:
  - 01-product-brief.md
  - 02-iteration-instructions.md
  - 03-task-board.md
  - 04-daily-work-log.md
  - 05-commit-convention.md
- [T-2026-04-12-006] Added Nx package scripts for simple startup:
  - npm run start (api + web-app)
  - npm run start:all (api + web-app)
  - npm run start:api
  - npm run start:web
- [T-2026-04-12-001] Completed persistence design note:
  - PostgreSQL-first data architecture documented
  - Redis/object storage support plan added
  - GitHub/GitLab/bare-repo integration strategy defined
- [T-2026-04-12-008] Added environment configuration:
  - .env for local development (in-memory database)
  - .env-template as safe reference (no secrets)
  - .gitignore rules for .env files in project-03
  - .gitignore created in parent folder for all projects
- [T-2026-04-12-007] Implemented database abstraction layer:
  - DatabaseConfig service for .env-based configuration
  - IProjectRepository interface for abstraction
  - InMemoryProjectRepository for dev mode
  - PostgreSQL repository with TypeORM entities
  - DatabaseService factory for selecting correct implementation
  - Updated ProjectsService to use abstraction
  - Updated AppModule and ProjectsModule to wire database
- [T-2026-04-12-009] Completed Angular template scaffold and execution flow:
  - Template payload now includes full Angular CLI-like structure
  - Added src/app/app.component.spec.ts and assets visibility files
  - Added favicon and angular.json assets alignment
  - On template load, auto-runs npm install + npm run start in WebContainer terminal
  - Ctrl+C support retained for process interruption in terminal
- [T-2026-04-12-010] Completed runtime UX hardening:
  - Added run stage indicator (preparing/installing/starting/running/error)
  - Added periodic heartbeat logs while install/start are running
  - Improved preview activation via URL parsing and shell output URL detection
  - Reduced noisy redraw behavior using no-progress flags for install/start
  - Added terminal auto-scroll and visible scrollbar styling
  - Added draggable resizing for explorer, editor/preview split, and terminal panel
- [T-2026-04-12-011] Completed shell flow type safety and reset stability:
  - Fixed TS2349 in app shell terminal flow by removing invalid never narrowing path
  - Refactored new terminal creation branch to keep callable writer typing intact
  - Revalidated app compile after fix (noEmit type check passed)
- [T-2026-04-12-012] Completed template startup resilience and unblock UX:
  - Added template action guard to prevent duplicate concurrent template starts
  - Improved Angular template lifecycle messages with explicit auto-start step
  - Added startup watchdog fallback to avoid indefinite blocking state during start
  - Added auto-open of preferred source file after scaffold/install to speed continuation
  - Unlocked template modal close behavior to prevent interaction dead-end
  - Added clearer terminal messaging when install/start is slow or fails

### Doing
- None.

### Next
- [T-2026-04-12-007] Implement PostgreSQL migrations and replace in-memory project store.
- [T-2026-04-12-002] Build package panel install flow.
- [T-2026-04-12-003] Add top bar Run and Install actions.
- [T-2026-04-12-004] Add notification/toast system.
- Add install-stage watchdog and structured run-log panel actions (clear/copy) as follow-up hardening.

### Blockers
- None currently.

### Notes
- Product direction remains: browser IDE inspired by StackBlitz and CodeSandbox.
