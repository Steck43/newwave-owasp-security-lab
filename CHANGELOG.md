# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Repo floor: required CI (secrets, authorship, tests, ruff, craft voice/changelog/comments), local pre-commit, Keep a Changelog.
- Floor template v2: push CI on every branch, `resolve_base.sh` (empty range exits 3), workflow lint (zizmor + actionlint), Dependabot (7-day cooldown), SECURITY.md. 

### Changed

- README leads with the attack a banking assistant can be talked into, states 2025-slug captures as fact rather than an order, and stops using Demonstrated for in-lab archives. That word stays reserved for external primary evidence on the dual-lab roof. 

### Fixed

- Floor CI: pin ruff to `>=0.15.15,<0.16` so GitHub cannot pull 0.16 default-rule expansion, and put repo-root `app.py` on `PYTHONPATH` for pytest. 
