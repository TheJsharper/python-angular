# Project-03 Iteration Instructions

This document defines what we did, what we are doing, what we should do next, and what we will do in planned iterations.

## Iteration Status Model
- Done: implemented and validated at least once.
- Doing: partially implemented or wired but incomplete in UX/robustness.
- Should Do: important backlog to reach MVP quality.
- Will Do: sequence of upcoming iterations.

## Done (What We Already Built)
### Platform foundation
- Nx workspace with three applications: web-app, api, api-e2e.
- Build and serve targets configured.

### API foundation
- NestJS app bootstrap with security and validation.
- Endpoints:
  - GET /api/templates
  - GET /api/templates/:id
  - GET /api/projects
  - GET /api/projects/:id
  - POST /api/projects
  - PUT /api/projects/:id
  - DELETE /api/projects/:id
  - GET /api/packages/search?q=...
  - GET /api/packages/:name

### Frontend foundation
- IDE shell with editor, terminal, preview, and file tree.
- Monaco and xterm integrated.
- Template selector wired to API.
- WebContainer boot + file operations + shell spawn.

## Doing (In Progress By Design)
### Product behavior currently available but not complete
- Editing flow works, but lacks robust save/dirty/version controls.
- Template loading works, but no explicit progress/retry UI.
- Terminal works, but command orchestration presets are missing.
- Preview is connected, but no clear run/start workflow button.
- Packages tab exists in UI state, but panel functionality is not yet complete.

### Stability and UX still maturing
- Error handling is basic (console logs and minimal UI feedback).
- No persistence beyond in-memory API store.
- No onboarding flow for first-time users.

## Should Do (Priority Backlog)
### P0 (MVP critical)
1. Implement project persistence in backend (database or file-based storage).
2. Complete package panel UI and install flow from search result to terminal command.
3. Add run/start command presets per template.
4. Add robust error surfaces (toast/errors panel) for API/WebContainer failures.
5. Add autosave policy and explicit save state indicators.

### P1 (High value)
1. Add project import/export (zip or gist-like JSON).
2. Add template boot diagnostics (dependency install status, missing scripts hints).
3. Improve file tree actions: rename, new file/folder, duplicate.
4. Add command history and keyboard shortcuts.
5. Strengthen API validation and contract tests.

### P2 (Scale and polish)
1. Session restore on refresh.
2. Shareable project links.
3. Better mobile fallback layout (read-only preview mode).
4. Optional auth and user project ownership.

## Will Do (Iteration Plan)
## Iteration 1 - MVP hardening
Goal: Make one-user local MVP reliable.

Tasks
1. Persistence layer for projects.
2. Finish package panel end-to-end install flow.
3. Implement top-level actions: Run, Install, Reset Template.
4. Add UI error boundary patterns.

Exit criteria
1. User can create project, refresh app, and recover project state.
2. User can search/install package from UI.
3. User sees actionable errors for failed operations.

## Iteration 2 - Productivity and confidence
Goal: Make development workflow smooth and testable.

Tasks
1. Add keyboard shortcuts and command palette basics.
2. Add template health checks and startup hints.
3. Expand test coverage:
   - API integration tests
   - web-app component tests for shell and template flows

Exit criteria
1. Core flows are covered by automated tests.
2. First-run friction reduced with guided hints.

## Iteration 3 - Share and collaboration readiness
Goal: Prepare product for external user trials.

Tasks
1. Export/import project bundle.
2. Share link model with server-side stored snapshots.
3. Performance pass on boot/load latency.

Exit criteria
1. User can share reproducible project state.
2. P95 template-to-preview time is within target.

## Working Agreement Per Iteration
For every iteration, execute this loop:
1. Define scope with max 5 deliverables.
2. Implement in small vertical slices (API + UI + tests).
3. Demo flows manually.
4. Record learnings and risks.
5. Re-plan next iteration based on measured outcomes.

## Definition of Done (DoD)
A task is done only when:
1. Feature behavior works in UI.
2. API contracts are validated.
3. Error path is handled.
4. Basic test coverage exists.
5. Documentation and iteration log are updated.

## Immediate Next Actions
1. Create persistence design note (storage choice, schema, migration path).
2. Implement package panel UI for search/install.
3. Add Run/Install buttons in top bar.
4. Add notification system for success/failure feedback.
