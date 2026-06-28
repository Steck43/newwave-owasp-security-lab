# Executive Summary

## NewWave OWASP Security Lab

Local Streamlit lab mapped to **OWASP LLM Top 10 (2025)**, **MITRE ATLAS**, and **NIST AI RMF**. It compares an intentionally unsafe investment-banking LLM assistant against a hardened configuration on the same attack prompt. NewWave is fictional. All deal data, clients, and tool actions are simulated text only.

## Method

Each run sends identical fictional context and user prompt to two instruction sets in parallel:

1. **Unsafe configuration**: follows user and document instructions with weak guardrails.
2. **Safe configuration**: treats retrieved content and user prompts as untrusted, blocks cross-client disclosure and prompt leakage, refuses external actions, and requires human review for high-risk finance outputs.

Responses come from live model APIs (OpenAI, Gemini, or OpenRouter). Wording varies by provider, model, and run.

## What was empirically tested (Phase 2)

Phase 2 captured **8 live runs** (4 scenarios, default and custom bypass prompt each) with provider Gemini and model `gemini-2.5-flash`. Verbatim outputs are in `evidence/phase2_capture.json`. Report tables and screenshots match those rows.

| Scenario | OWASP LLM 2025 | MITRE ATLAS |
| --- | --- | --- |
| Prompt Injection | LLM01 | AML.T0051; indirect AML.T0051.001 |
| Sensitive Information Disclosure | LLM02 | AML.T0057 LLM Data Leakage |
| Excessive Agency | LLM06 | |
| System Prompt Leakage | LLM07 | AML.T0056 Extract LLM System Prompt |

Observed pattern in archived runs: the unsafe configuration followed injected framing, disclosed cross-client data, leaked internal-style policy text, and showed phrasing-sensitive agency behavior. The safe configuration refused or contained those classes.

## Phase 3 status (blocked)

Three scenarios were added for LLM05 Improper Output Handling, LLM09 Misinformation, and LLM10 Unbounded Consumption. Capture script: `tools/capture_phase3_evidence.py`. **Capture did not complete** on 2026-06-28 because `GEMINI_API_KEY` returned `API_KEY_INVALID`. No `phase3_capture.json` exists. See `evidence/phase3_capture_status.md`.

## Honest coverage (Section 5.1 status language)

| Status | Count | Risks |
| --- | --- | --- |
| Demonstrated | 4 of 10 | LLM01, LLM02, LLM06, LLM07 |
| Assessed-not-demonstrated (architectural note) | 1 | LLM03 ([note](evidence/llm03_supply_chain_assessment.md)) |
| Assessed-not-demonstrated (capture pending) | 3 | LLM05, LLM09, LLM10 (scenarios in app) |
| Assessed-not-demonstrated (planned) | 2 | LLM04, LLM08 |

**Target after valid Phase 3 capture**: 7 Demonstrated (add LLM05, LLM09, LLM10).

**OWASP Top 10 for Agentic Applications 2026**: in progress, not shipped.

## NIST AI RMF mapping (report Section 10.3 pattern)

| Function | Application in this lab |
| --- | --- |
| Govern | Human review required for high-impact finance outputs in safe configuration |
| Map | Fictional assets, trust boundaries, OWASP coverage matrix |
| Measure | Phase 2 adversarial capture set (8 runs); Phase 3 pending |
| Manage | Safe vs unsafe control comparison drives mitigation priorities |

## Control mapping approach

Safe controls are extracted from `SAFE_ASSISTANT_INSTRUCTIONS` in `app.py` and mapped to OWASP risks in `evidence/safe_controls_to_owasp.md`. Input separation via tagged context and prompt regions is in `evidence/input_separation_control.md`. Prompt-level controls are probabilistic under adversarial phrasing. Deterministic gates outside the model remain the final enforcement boundary for regulated workflows.

## References

- [Coverage matrix](owasp_coverage.md)
- [Evidence index](README.md)
- OWASP LLM Top 10 2025 and Agentic Top 10 2026 (CC BY-SA 4.0). See repository README for citation links.
