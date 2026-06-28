# Executive Summary

## NewWave OWASP Security Lab

Local Streamlit lab that compares an intentionally unsafe investment-banking LLM assistant against a hardened configuration on the same attack prompt. NewWave is fictional. All deal data, clients, and tool actions are simulated text only.

## Method

Each run sends identical fictional context and user prompt to two instruction sets in parallel:

1. **Unsafe configuration**: follows user and document instructions with weak guardrails.
2. **Safe configuration**: treats retrieved content and user prompts as untrusted, blocks cross-client disclosure and prompt leakage, refuses external actions, and requires human review for high-risk finance outputs.

Responses come from live model APIs (OpenAI, Gemini, or OpenRouter). Wording varies by provider, model, and run.

## What was empirically tested

Phase 2 captured **8 live runs** (4 scenarios, default and custom bypass prompt each) with provider Gemini and model `gemini-2.5-flash`. Verbatim outputs are in `evidence/phase2_capture.json`. Report tables and screenshots match those rows.

| Scenario | OWASP LLM 2025 |
| --- | --- |
| Prompt Injection | LLM01 |
| Sensitive Information Disclosure | LLM02 |
| Excessive Agency | LLM06 |
| System Prompt Leakage | LLM07 |

Observed pattern: the unsafe configuration followed injected framing, disclosed cross-client data, leaked internal-style policy text, and showed phrasing-sensitive agency behavior. The safe configuration refused or contained those classes in the archived runs.

## Honest coverage

**4 of 10** OWASP LLM Top 10 (2025) risks are **Demonstrated** with on-disk capture and screenshots. The other six risks are listed in [owasp_coverage.md](owasp_coverage.md) as **Architectural** (control mapping or gap only). LLM09 has one safe-instruction mapping line but no dedicated scenario or capture.

**OWASP Top 10 for Agentic Applications 2026** is marked in progress. This repo does not yet ship agentic scenarios or ASI evidence.

## Control mapping approach

Safe controls are extracted from `SAFE_ASSISTANT_INSTRUCTIONS` in `app.py` and mapped to OWASP risks in `evidence/safe_controls_to_owasp.md`. Input separation via tagged context and prompt regions is documented in `evidence/input_separation_control.md`. Prompt-level controls are probabilistic under adversarial phrasing. Deterministic gates outside the model remain the final enforcement boundary for regulated workflows.

## References

- [Coverage matrix](owasp_coverage.md)
- [Evidence index](README.md)
- OWASP LLM Top 10 2025 and Agentic Top 10 2026 (CC BY-SA 4.0). See repository README for citation links.
