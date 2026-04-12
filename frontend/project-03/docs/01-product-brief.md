# Project-03 Product Brief

## Vision
Project-03 is a browser IDE inspired by StackBlitz and CodeSandbox.

The goal is to let a developer start from a template, edit files, run commands, preview the app, and iterate without local setup friction.

## Product Type
- Full-stack monorepo (Nx)
- Frontend: Angular app (IDE-like UI)
- Backend: NestJS API (templates, project metadata, package lookup)
- Runtime engine: WebContainer API for in-browser execution

## Problem It Solves
- Slow project bootstrap when trying ideas.
- Context switching between editor, terminal, and preview.
- Repeating boilerplate setup for new experiments.
- Unsafe direct client calls to package registries.

## Current Scope (Implemented)
### Frontend (web-app)
- IDE shell layout with:
  - Activity bar
  - File tree sidebar
  - Editor tabs
  - Terminal panel
  - Preview panel
- Monaco editor integration.
- xterm terminal integration.
- Template selection modal.
- File open/edit/delete flows wired to WebContainer filesystem.

### Backend (api)
- API boot with:
  - CORS configuration
  - Helmet security middleware
  - COOP/COEP headers for cross-origin isolation
  - Validation pipes
  - Global prefix: /api
- Projects module:
  - Create/read/update/delete project metadata and files (in-memory store)
- Templates module:
  - List templates
  - Fetch template details with scaffold files
- Packages module:
  - Search npm registry
  - Fetch package metadata with package-name validation and timeout

### Quality / Ops
- API e2e scaffold with Jest.
- Nx targets for build/serve/test/lint.

## Current Reality Check
- Core architecture exists and boots.
- Main UI structure exists.
- Template and package APIs exist.
- Data persistence is not yet durable (projects are in memory only).
- Collaboration/auth/version history features are not implemented yet.

## North Star Experience
1. User opens DevBox in browser.
2. Picks template (Angular/React/Vue/Node/Nest).
3. Code appears instantly.
4. User edits, installs package, runs app.
5. Live preview refreshes quickly.
6. User can save/share/export project.

## Non-Goals (For Now)
- Real-time multiplayer editing.
- Full Git provider integration.
- Marketplace-level deployment pipeline.
- Enterprise RBAC and billing.

## Success Metrics
- Time to first preview under 30 seconds on warm path.
- Template load success rate above 99%.
- Command execution feedback visible in terminal in under 500 ms.
- API error rate below 1% for template/package endpoints.
