# OWASP Coverage Matrix

NewWave OWASP Security Lab. Mapped to OWASP LLM Top 10 (2025), MITRE ATLAS where noted below, and NIST AI RMF (see executive summary). Status values follow the course report Section 5.1 demo-status language.

**Demonstrated count**: **7 of 10** OWASP LLM Top 10 (2025) risks.

Claim boundaries: [scope-and-limitations.md](scope-and-limitations.md).

## Status definitions (Section 5.1)

| Status | Meaning |
| --- | --- |
| Demonstrated | Live model capture and matching screenshots under `evidence/` |
| Assessed-not-demonstrated (architectural note) | Threat and control notes only, no live exploit |
| Assessed-not-demonstrated (planned) | Listed in scope, no scenario or capture yet |

## LLM Top 10 (2025)

| LLM ID | Official title | Scenario | Status | MITRE ATLAS | Evidence path |
| --- | --- | --- | --- | --- | --- |
| LLM01 | Prompt Injection | Prompt Injection | Demonstrated | AML.T0051; indirect AML.T0051.001 | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/prompt_injection_*.png`, `evidence/input_separation_control.md` |
| LLM02 | Sensitive Information Disclosure | Sensitive Information Disclosure | Demonstrated | AML.T0057 LLM Data Leakage | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/sensitive_information_disclosure_*.png` |
| LLM03 | Supply Chain | Not implemented | Assessed-not-demonstrated (architectural note) | | `evidence/llm03_supply_chain_assessment.md` |
| LLM04 | Data and Model Poisoning | Not implemented | Assessed-not-demonstrated (planned) | | none (gap) |
| LLM05 | Improper Output Handling | Improper Output Handling | Demonstrated | | `evidence/phase3_capture.json`, `evidence/phase3_evidence_table.md`, `evidence/screenshots/improper_output_handling_*.png` |
| LLM06 | Excessive Agency | Excessive Agency | Demonstrated | | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/excessive_agency_*.png` |
| LLM07 | System Prompt Leakage | System Prompt Leakage | Demonstrated | AML.T0056 Extract LLM System Prompt | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/system_prompt_leakage_*.png` |
| LLM08 | Vector and Embedding Weaknesses | Not implemented | Assessed-not-demonstrated (planned) | | none (gap) |
| LLM09 | Misinformation | Misinformation | Demonstrated | AML.T0048 External Harms | `evidence/phase3_capture.json`, `evidence/phase3_evidence_table.md`, `evidence/screenshots/misinformation_*.png` |
| LLM10 | Unbounded Consumption | Unbounded Consumption | Demonstrated | | `evidence/phase3_capture.json`, `evidence/phase3_evidence_table.md`, `evidence/screenshots/unbounded_consumption_*.png` |

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
