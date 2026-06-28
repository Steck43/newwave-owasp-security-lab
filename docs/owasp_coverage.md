# OWASP Coverage Matrix

NewWave OWASP Security Lab. Mapped to OWASP LLM Top 10 (2025), MITRE ATLAS where noted below, and NIST AI RMF (see executive summary). Status values follow the course report Section 5.1 demo-status language.

**Demonstrated count today**: **4 of 10** (Phase 2 capture on disk). Phase 3 scenarios exist in `app.py` but capture is blocked pending a valid API key. See `evidence/phase3_capture_status.md`.

## Status definitions (Section 5.1)

| Status | Meaning |
| --- | --- |
| Demonstrated | Live model capture and matching screenshots under `evidence/` |
| Assessed-not-demonstrated (architectural note) | Threat and control notes only, no live exploit |
| Assessed-not-demonstrated (planned) | Listed in scope, no scenario or capture yet |
| Assessed-not-demonstrated (capture pending) | Scenario in app, capture script ready, no capture file yet |

## LLM Top 10 (2025)

| LLM ID | Official title | Scenario | Status | MITRE ATLAS | Evidence path |
| --- | --- | --- | --- | --- | --- |
| LLM01 | Prompt Injection | Prompt Injection | Demonstrated | AML.T0051; indirect AML.T0051.001 | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/prompt_injection_*.png`, `evidence/input_separation_control.md` |
| LLM02 | Sensitive Information Disclosure | Sensitive Information Disclosure | Demonstrated | AML.T0057 LLM Data Leakage | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/sensitive_information_disclosure_*.png` |
| LLM03 | Supply Chain | Not implemented | Assessed-not-demonstrated (architectural note) | | `evidence/llm03_supply_chain_assessment.md` |
| LLM04 | Data and Model Poisoning | Not implemented | Assessed-not-demonstrated (planned) | | none (gap) |
| LLM05 | Improper Output Handling | Improper Output Handling | Assessed-not-demonstrated (capture pending) | | `evidence/phase3_capture_status.md` |
| LLM06 | Excessive Agency | Excessive Agency | Demonstrated | | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/excessive_agency_*.png` |
| LLM07 | System Prompt Leakage | System Prompt Leakage | Demonstrated | AML.T0056 Extract LLM System Prompt | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/system_prompt_leakage_*.png` |
| LLM08 | Vector and Embedding Weaknesses | Not implemented | Assessed-not-demonstrated (planned) | | none (gap) |
| LLM09 | Misinformation | Misinformation | Assessed-not-demonstrated (capture pending) | AML.T0048 External Harms | `evidence/safe_controls_to_owasp.md`, `evidence/phase3_capture_status.md` |
| LLM10 | Unbounded Consumption | Unbounded Consumption | Assessed-not-demonstrated (capture pending) | | `evidence/phase3_capture_status.md` |

## Cross-cutting control mapping

| Artifact | Scope |
| --- | --- |
| `evidence/safe_controls_to_owasp.md` | Safe instruction lines mapped to LLM01, LLM02, LLM05, LLM06, LLM07, LLM09, LLM10 |
| `evidence/input_separation_control.md` | `build_llm_input()` trust boundary (LLM01) |

## Agentic Top 10 (2026)

| Framework | Status |
| --- | --- |
| OWASP Top 10 for Agentic Applications 2026 (ASI01 through ASI10) | In progress, not shipped |

## Reference standards

- OWASP Top 10 for LLM Applications 2025, published 2024-11-18, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- OWASP Top 10 for Agentic Applications 2026, published 2025-12, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## Target state after Phase 3 capture

When `evidence/phase3_capture.json` and screenshots exist, LLM05, LLM09, and LLM10 move to **Demonstrated** for a total of **7 of 10**. LLM03 remains Assessed-not-demonstrated (architectural note). LLM04 and LLM08 remain Assessed-not-demonstrated (planned).
