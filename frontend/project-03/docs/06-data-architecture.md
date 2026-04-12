# Project-03 Data Architecture

## Decision
Use PostgreSQL as the primary database.

## Why PostgreSQL First
1. Strong transactional consistency for user, project, workspace, and permission updates.
2. Relational modeling matches product needs (users, orgs, repos, memberships, snapshots, jobs).
3. JSONB supports flexible metadata without forcing a separate document database early.
4. Good ecosystem for migrations, indexing, observability, and backup/recovery.

## Recommended Multi-Store Architecture
### Primary
- PostgreSQL: source of truth for product/business data.

### Supporting
- Redis: cache, rate limit counters, background queue coordination, session acceleration.
- Object Storage (S3/MinIO): project archives, snapshot bundles, logs/artifacts.

### Optional Later
- OpenSearch/Elasticsearch for fast code/content search if needed.
- Graph database only if advanced dependency/contributor graph analytics become core.

## What Not To Do Now
1. Do not make a document database the primary system of record.
2. Do not introduce graph DB before clear query bottlenecks justify it.

## Git Provider and Bare Repo Strategy
Keep git content in git repositories, not as large blobs in SQL rows.

Store in PostgreSQL:
1. Provider metadata (github/gitlab/self-hosted).
2. Repository connection details (owner, repo, default branch, sync status).
3. Credential references (token secret IDs, not raw secrets).
4. Sync job records and outcomes.
5. Snapshot/version metadata.

Use workers for:
1. Clone/fetch/push operations.
2. Webhook processing.
3. Mirror sync and conflict handling.

## Initial Domain Model (MVP)
1. users
2. organizations
3. organization_members
4. projects
5. workspaces
6. repositories
7. provider_accounts
8. workspace_snapshots
9. repo_sync_jobs
10. audit_events

## Iteration Plan For Persistence
### Iteration 1 (Now)
1. Implement PostgreSQL connection and migration tooling.
2. Replace in-memory projects store with PostgreSQL-backed repository.
3. Add audit events for project CRUD.

### Iteration 2
1. Add repository/provider account tables and webhook ingest.
2. Add snapshot storage metadata and export/import path.

### Iteration 3
1. Add advanced indexing/search and operational dashboards.

## Acceptance Criteria
1. Project CRUD survives API restarts.
2. Migrations are versioned and reversible.
3. Provider integration model supports GitHub, GitLab, and bare repos.
4. No raw secrets stored in application tables.
