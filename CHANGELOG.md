# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Capture-evidence prove: required keys plus a locked git-blob hash for phase2 and phase3 JSON. The lock is the index bytes, not the Windows worktree. An empty or swapped file fails the clone.
- CITATION.cff and `.zenodo.json` so a later tag can mint. No DOI on this record yet.
- Architectural notes for LLM04 and LLM08. ASI01–ASI10 stay cited to `owasp-dual-top10-lab` `labctl`; this roof does not clone that fixture engine.
- Repo floor: required CI (secrets, authorship, tests, ruff, craft voice/changelog/comments), local pre-commit, Keep a Changelog.
- Floor template v2: push CI on every branch, `resolve_base.sh` (empty range exits 3), workflow lint (zizmor + actionlint), Dependabot (7-day cooldown), SECURITY.md.

### Changed

- Coverage lead drops Demonstrated 7 of 10. Seven live captures, three notes, ASI cited at the dual-lab GitHub URL. This lab's Reproduced-in-lab is Section 5.1, not the dual-lab machine gate.
- CITATION.cff and `.zenodo.json` name Wenhan Kong for the `cda59f1` base demo, matching LICENSE.
- README leads with the attack a banking assistant can be talked into, states 2025-slug captures as fact rather than an order, and stops using Demonstrated for in-lab archives. That word stays reserved for external primary evidence on the dual-lab roof.

### Fixed

- First push of a new branch resolves craft BASE to the origin default, so required craft jobs do not fail on an all-zero `github.event.before`.
- Floor CI: pin ruff to `>=0.15.15,<0.16` so GitHub cannot pull 0.16 default-rule expansion, and put repo-root `app.py` on `PYTHONPATH` for pytest.
