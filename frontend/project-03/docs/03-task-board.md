# Project-03 Task Board

## Status Legend
- TODO: not started
- DOING: in progress
- DONE: completed and verified
- BLOCKED: waiting for dependency/decision

## Active Iteration
- Iteration ID: ITER-2026-04-I1
- Start date: 2026-04-12
- Goal: MVP hardening for StackBlitz/CodeSandbox-inspired flow

## Tasks
| Task ID | Title | Priority | Status | Owner | Start Date | Due Date | Done Date | Notes |
|---|---|---|---|---|---|---|---|---|
| T-2026-04-12-001 | Persistence design note | P0 | DONE | Pedro/Copilot | 2026-04-12 | 2026-04-13 | 2026-04-12 | PostgreSQL-first architecture documented in 06-data-architecture.md |
| T-2026-04-12-002 | Package panel end-to-end | P0 | TODO | Pedro/Copilot | 2026-04-12 | 2026-04-14 | - | Search, select, install command, feedback |
| T-2026-04-12-003 | Run and Install top actions | P0 | TODO | Pedro/Copilot | 2026-04-12 | 2026-04-14 | - | Add top bar actions and command presets |
| T-2026-04-12-004 | UI notifications/errors | P0 | TODO | Pedro/Copilot | 2026-04-12 | 2026-04-14 | - | Unified success/error toasts |
| T-2026-04-12-005 | Iteration docs baseline | P0 | DONE | Copilot | 2026-04-12 | 2026-04-12 | 2026-04-12 | Product brief + iteration instructions + this task system |
| T-2026-04-12-006 | Nx start scripts for both apps | P0 | DONE | Copilot | 2026-04-12 | 2026-04-12 | 2026-04-12 | Added package scripts to run api + web-app together |
| T-2026-04-12-007 | PostgreSQL persistence implementation | P0 | DONE | Copilot | 2026-04-12 | 2026-04-12 | 2026-04-12 | Database abstraction layer with in-memory and PostgreSQL support |
| T-2026-04-12-008 | Environment configuration (.env/.env-template) | P0 | DONE | Copilot | 2026-04-12 | 2026-04-12 | 2026-04-12 | Dev: in-memory, Prod: PostgreSQL config with .gitignore |
| T-2026-04-12-009 | Angular template full scaffold + auto-run | P0 | DONE | Copilot | 2026-04-12 | 2026-04-12 | 2026-04-12 | Template now includes full Angular CLI-like files/folders; auto runs install/start in WebContainer terminal |
| T-2026-04-12-010 | Runtime UX hardening (logs/preview/layout) | P0 | DONE | Copilot | 2026-04-12 | 2026-04-12 | 2026-04-12 | Added progress indicators, heartbeat logs, preview URL fallback, terminal scrollbar, and draggable explorer/split/terminal |
| T-2026-04-12-011 | Shell flow type safety and reset stability | P0 | DONE | Copilot | 2026-04-12 | 2026-04-12 | 2026-04-12 | Fixed TS2349 never-call issue in newTerminal and stabilized shell reset/new terminal behavior |
| T-2026-04-12-012 | Template startup resilience and unblock UX | P0 | DONE | Copilot | 2026-04-12 | 2026-04-12 | 2026-04-12 | Added stronger template progress states, startup watchdog recovery, modal unblock behavior, and auto-open of main workspace file |

## How To Update
1. Always create a new Task ID using: T-YYYY-MM-DD-XXX.
2. Move status sequentially: TODO -> DOING -> DONE.
3. Fill Done Date when status becomes DONE.
4. Reference Task IDs in commit messages.
