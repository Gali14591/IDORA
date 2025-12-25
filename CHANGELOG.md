# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-12-25
### Added
- CI workflow (GitHub Actions) to install dependencies, run migrations and tests.
- Dockerfile and docker-compose for local development.
- Basic API endpoints for accounts, documents, sends, inbox, and audit.
- Unit tests covering registration, document ownership and end-to-end flows.

### Fixed
- Corrected CI working directory for Django management commands (now runs from repo root).
