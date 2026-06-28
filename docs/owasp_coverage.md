# OWASP Coverage Matrix

NewWave OWASP Security Lab. Coverage is mapped from files on disk only.

**Tiers**

- **Demonstrated**: live model capture and matching screenshots exist under `evidence/`.
- **Simulated**: runnable in the Streamlit app, lab-only, no archived capture set for that risk.
- **Architectural**: control mapping or threat notes only, no dedicated scenario or exploit demo.

**Demonstrated count**: 4 of 10 OWASP LLM Top 10 (2025) risks.

| LLM ID | Official title | Scenario | Tier | Evidence path |
| --- | --- | --- | --- | --- |
| LLM01 | Prompt Injection | Prompt Injection | Demonstrated | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/prompt_injection_default.png`, `evidence/screenshots/prompt_injection_custom.png`, `evidence/input_separation_control.md` |
| LLM02 | Sensitive Information Disclosure | Sensitive Information Disclosure | Demonstrated | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/sensitive_information_disclosure_default.png`, `evidence/screenshots/sensitive_information_disclosure_custom.png` |
| LLM03 | Supply Chain | Not implemented | Architectural | none (gap) |
| LLM04 | Data and Model Poisoning | Not implemented | Architectural | none (gap) |
| LLM05 | Improper Output Handling | Not implemented | Architectural | none (gap) |
| LLM06 | Excessive Agency | Excessive Agency | Demonstrated | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/excessive_agency_default.png`, `evidence/screenshots/excessive_agency_custom.png` |
| LLM07 | System Prompt Leakage | System Prompt Leakage | Demonstrated | `evidence/phase2_capture.json`, `evidence/phase2_evidence_table.md`, `evidence/screenshots/system_prompt_leakage_default.png`, `evidence/screenshots/system_prompt_leakage_custom.png` |
| LLM08 | Vector and Embedding Weaknesses | Not implemented | Architectural | none (gap) |
| LLM09 | Misinformation | Not implemented (control line only) | Architectural | `evidence/safe_controls_to_owasp.md` (instruction mapping only, no scenario or capture) |
| LLM10 | Unbounded Consumption | Not implemented | Architectural | none (gap) |

## Cross-cutting control mapping

| Artifact | Scope |
| --- | --- |
| `evidence/safe_controls_to_owasp.md` | Safe instruction lines in `app.py` mapped to LLM01, LLM02, LLM06, LLM07, LLM09 |
| `evidence/input_separation_control.md` | `build_llm_input()` trust boundary (supports LLM01) |

## Agentic Top 10 (2026)

| Framework | Status | Notes |
| --- | --- | --- |
| OWASP Top 10 for Agentic Applications 2026 (ASI01 through ASI10) | In progress, not shipped | No agentic scenarios, tool registry, or ASI capture set in this repo yet. Planned extension of the same NewWave assistant model. |

## Reference standards

- OWASP Top 10 for LLM Applications 2025, published 2024-11-18, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- OWASP Top 10 for Agentic Applications 2026, published 2025-12, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
