# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Repo floor: required CI (secrets, authorship, tests, ruff, craft voice/changelog/comments), local pre-commit, Keep a Changelog.
- Floor template v2: push CI on every branch, `resolve_base.sh` (empty range exits 3), workflow lint (zizmor + actionlint), Dependabot, SECURITY.md. 

### Changed

- 

### Fixed

- Floor CI: pin ruff to `>=0.15.15,<0.16` so GitHub cannot pull 0.16 default-rule expansion, and put repo-root `app.py` on `PYTHONPATH` for pytest. 
