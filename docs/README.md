# Documentation Index

Portfolio-facing docs for the NewWave OWASP Security Lab.

## Start here

| Document | Purpose |
| --- | --- |
| [executive-summary.md](executive-summary.md) | One-page overview for resume and LinkedIn |
| [owasp_coverage.md](owasp_coverage.md) | OWASP LLM 2025 coverage matrix with honest tiers |

## Evidence artifacts

Primary capture and analysis files live under `../evidence/`.

| Path | Contents |
| --- | --- |
| [../evidence/phase2_capture.json](../evidence/phase2_capture.json) | Verbatim 8-run capture (LLM01, LLM02, LLM06, LLM07) |
| [../evidence/phase2_evidence_table.md](../evidence/phase2_evidence_table.md) | Report-ready table for Phase 2 |
| [../evidence/phase3_capture.json](../evidence/phase3_capture.json) | Verbatim 6-run capture (LLM05, LLM09, LLM10) |
| [../evidence/phase3_evidence_table.md](../evidence/phase3_evidence_table.md) | Report-ready table for Phase 3 |
| [../evidence/safe_controls_to_owasp.md](../evidence/safe_controls_to_owasp.md) | Safe instruction lines mapped to OWASP LLM risks |
| [../evidence/input_separation_control.md](../evidence/input_separation_control.md) | `build_llm_input()` trusted vs untrusted separation |
| [../evidence/audit_closed_checklist.md](../evidence/audit_closed_checklist.md) | Phase 2 scope and completion checklist |
| [../evidence/llm03_supply_chain_assessment.md](../evidence/llm03_supply_chain_assessment.md) | LLM03 architectural supply-chain note |
| [../evidence/phase3_capture_status.md](../evidence/phase3_capture_status.md) | Phase 3 capture blocker and rerun steps |
| [../evidence/screenshots/README.md](../evidence/screenshots/README.md) | Screenshot index |

### Screenshot panels

Generated from `phase2_capture.json`. One default and one custom panel per demonstrated scenario.

- `evidence/screenshots/prompt_injection_*.png` (LLM01)
- `evidence/screenshots/sensitive_information_disclosure_*.png` (LLM02)
- `evidence/screenshots/system_prompt_leakage_*.png` (LLM07)
- `evidence/screenshots/excessive_agency_*.png` (LLM06)
- `evidence/screenshots/improper_output_handling_*.png` (LLM05)
- `evidence/screenshots/misinformation_*.png` (LLM09)
- `evidence/screenshots/unbounded_consumption_*.png` (LLM10)
- `evidence/screenshots/provenance_panel.png` (Phase 2 metadata)
- `evidence/screenshots/provenance_panel_phase3.png` (Phase 3 metadata)
- `evidence/screenshots/Anchor.png` (layout reference)

## Report drafts (course artifacts)

These supported the original security assessment write-up. They are not live capture evidence.

| Path | Contents |
| --- | --- |
| [../evidence/report_outline_revised.md](../evidence/report_outline_revised.md) | Evidence-aligned report outline |
| [../evidence/report_draft_shell.md](../evidence/report_draft_shell.md) | Report draft shell |

## Tools

| Path | Contents |
| --- | --- |
| [../tools/generate_evidence_screenshots.py](../tools/generate_evidence_screenshots.py) | Regenerate screenshot panels from a capture JSON |
| [../tools/capture_phase3_evidence.py](../tools/capture_phase3_evidence.py) | Run Phase 3 live captures to `phase3_capture.json` |
