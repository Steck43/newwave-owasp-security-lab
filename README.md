# NewWave OWASP Security Lab

This lab is the **OWASP LLM Top 10 2025** edition. Directory IDs and Demonstrated captures stay on 2025 slugs. Do not rebase those captures onto the 2026 list (LLM08:2025 Vector is not LLM08:2026 Hidden Context Exposure).

OWASP LLM Top 10 (2025) security lab for regulated finance, mapped to OWASP LLM Top 10, MITRE ATLAS, and NIST AI RMF. Unsafe vs hardened investment-banking assistant with live model evidence and OWASP control mapping.

Local Streamlit demo. Same fictional attack prompt runs against two instruction sets side by side: an intentionally unsafe configuration and a safer banking-oriented configuration. Responses come from real model APIs, not hardcoded text.

**Coverage**: **7 of 10** OWASP LLM risks are **Demonstrated** with archived capture and screenshots. LLM03 has an architectural assessment note. LLM04 and LLM08 are Assessed-not-demonstrated (planned). See the [coverage matrix](docs/owasp_coverage.md) and [evidence index](docs/README.md). [Executive summary](docs/executive-summary.md) includes scope and limitations inline.

**In progress**: [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org) (ASI01 through ASI10). Not shipped in this repo yet.

## Demonstrated scenarios

| Scenario | OWASP LLM 2025 | Capture | MITRE ATLAS |
| --- | --- | --- | --- |
| Prompt Injection | LLM01 | Phase 2 | AML.T0051; indirect AML.T0051.001 |
| Sensitive Information Disclosure | LLM02 | Phase 2 | AML.T0057 LLM Data Leakage |
| Improper Output Handling | LLM05 | Phase 3 | no clean 1-to-1 |
| Excessive Agency | LLM06 | Phase 2 | no clean 1-to-1 |
| System Prompt Leakage | LLM07 | Phase 2 | AML.T0056 Extract LLM System Prompt |
| Misinformation | LLM09 | Phase 3 | |
| Unbounded Consumption | LLM10 | Phase 3 | no clean 1-to-1 |

Evidence: [phase2 capture](evidence/phase2_capture.json), [phase3 capture](evidence/phase3_capture.json), [screenshots](evidence/screenshots/README.md).

## Assessed-not-demonstrated

| LLM ID | Status | Notes |
| --- | --- | --- |
| LLM03 Supply Chain | Architectural note | [Assessment](evidence/llm03_supply_chain_assessment.md) |
| LLM04 Data and Model Poisoning | Planned | |
| LLM08 Vector and Embedding Weaknesses | Planned | |

Control mapping: [safe controls to OWASP](evidence/safe_controls_to_owasp.md), [input separation](evidence/input_separation_control.md).

## Safety scope

NewWave is a fictional Bay Area investment bank. All clients, deal names, buyer lists, financial figures, documents, and risks are fictional.

The app does not send emails, modify files, connect to external systems, call financial APIs, or perform real financial actions. Email and tool behavior is simulated text only.

## Install

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configure API keys

Copy the example env file and add your keys:

```bash
cp .env.example .env
```

Supported providers: OpenAI (`OPENAI_API_KEY`), Gemini (`GEMINI_API_KEY` or `GOOGLE_API_KEY`), OpenRouter (`OPENROUTER_API_KEY`). Streamlit secrets in `.streamlit/secrets.toml` are also supported.

## Run

```bash
streamlit run app.py
```

Default provider is Gemini. Change provider and model name in the sidebar. Override defaults with `DEFAULT_PROVIDER`, `DEFAULT_GEMINI_MODEL`, `DEFAULT_OPENAI_MODEL`, or `DEFAULT_OPENROUTER_MODEL` in `.env`.

## What the demo shows

- **Unsafe configuration**: intentionally vulnerable classroom simulation.
- **Safe configuration**: untrusted input handling, disclosure blocks, draft-only external actions, human review for high-risk outputs.
- Both configurations stream in parallel for direct comparison.

Exact wording varies by provider, model, and run.

## Repository layout

```text
app.py                 Streamlit demo (unsafe vs safe)
docs/                  Coverage matrix, executive summary, doc index
evidence/              Phase 2 and Phase 3 capture, tables, screenshots
tools/                 Capture and screenshot scripts
```

## References

This project maps to:

- **OWASP Top 10 for LLM Applications 2025** (published 2024-11-18), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **OWASP Top 10 for Agentic Applications 2026** (published 2025-12), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **MITRE ATLAS** (technique IDs cited in coverage matrix where verified)
- **NIST AI RMF 1.0** (Govern, Map, Measure, Manage; see executive summary)

Official project pages: [genai.owasp.org](https://genai.owasp.org)

## Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md). The base NewWave Streamlit demo (`cda59f1`) is by Wenhan Kong. The security assessment, added scenarios, evidence, and portfolio documentation are by Landen Stecker.

## License

MIT License. Copyright (c) 2026 Landen Stecker covers the security assessment, documentation, evidence, scenarios and code added after the base commit, and related tooling. The base demo application is authored by Wenhan Kong. See [LICENSE](LICENSE).

OWASP standards are cited as references under CC BY-SA 4.0 and are not relicensed under MIT.

---

_Originally developed for CSEN 296A-1 Security in AI, Spring 2026._
