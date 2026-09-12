# NewWave OWASP Security Lab

A banking assistant that sees a deal memo can be talked into leaking it, drafting a transfer, or treating a forged price as fact. This lab runs the same fictional attack prompt against two instruction sets, an intentionally unsafe configuration and a safer banking-oriented one, and records what a live model actually returns. The responses come from real model APIs, not hardcoded text.

The directory is the OWASP LLM Top 10 2025 edition. Captures stay on 2025 slugs because LLM08:2025 Vector is not LLM08:2026 Hidden Context Exposure, and a capture taken against one list is not evidence against the other.

Seven live captures, three architectural notes, ASI cited next door. Demonstrated stays the external-primary pin. Coverage, evidence, and scope live in the [coverage matrix](docs/owasp_coverage.md), the [evidence index](docs/README.md), and the [executive summary](docs/executive-summary.md).

The [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org) (ASI01 through ASI10) is cited, not shipped here. Run `labctl` against `owasp-dual-top10-lab/scenarios/asi/`. Do not clone that fixture engine into this roof.

## Archived in-lab captures

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

## Assessed, not captured

| LLM ID | Status | Notes |
| --- | --- | --- |
| LLM03 Supply Chain | Architectural note | [Assessment](evidence/llm03_supply_chain_assessment.md) |
| LLM04 Data and Model Poisoning | Architectural note | [Assessment](evidence/llm04_data_poisoning_assessment.md) |
| LLM08 Vector and Embedding Weaknesses | Architectural note | [Assessment](evidence/llm08_vector_embedding_assessment.md) |

Control mapping: [safe controls to OWASP](evidence/safe_controls_to_owasp.md), [input separation](evidence/input_separation_control.md).

## Safety scope

NewWave is a fictional Bay Area investment bank; all clients, deal names, buyer lists, financial figures, documents, and risks are fictional. The app does not send emails, modify files, connect to external systems, call financial APIs, or perform real financial actions, and email and tool behavior is simulated text only.

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

Supported providers are OpenAI (`OPENAI_API_KEY`), Gemini (`GEMINI_API_KEY` or `GOOGLE_API_KEY`), and OpenRouter (`OPENROUTER_API_KEY`); Streamlit secrets in `.streamlit/secrets.toml` are also accepted.

## Run

```bash
streamlit run app.py
```

Default provider is Gemini; change provider and model name in the sidebar, or override `DEFAULT_PROVIDER`, `DEFAULT_GEMINI_MODEL`, `DEFAULT_OPENAI_MODEL`, or `DEFAULT_OPENROUTER_MODEL` in `.env`.

## What the demo shows

- **Unsafe configuration**: intentionally vulnerable classroom simulation.
- **Safe configuration**: untrusted input handling, disclosure blocks, draft-only external actions, human review for high-risk outputs.
- Both configurations stream in parallel for direct comparison, and exact wording varies by provider, model, and run.

## Repository layout

```text
app.py                 Streamlit demo (unsafe vs safe)
docs/                  Coverage matrix, executive summary, doc index
evidence/              Phase 2 and Phase 3 capture, tables, screenshots
tools/                 Capture and screenshot scripts
```

## References

This project maps to OWASP Top 10 for LLM Applications 2025, OWASP Top 10 for Agentic Applications 2026, MITRE ATLAS, and NIST AI RMF 1.0, under the terms those projects publish at [genai.owasp.org](https://genai.owasp.org).

## Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md). The base NewWave Streamlit demo (`cda59f1`) is by Wenhan Kong; the security assessment, added scenarios, evidence, and portfolio documentation are by Landen Stecker.

## License

MIT License. Copyright (c) 2026 Landen Stecker covers the security assessment, documentation, evidence, scenarios and code added after the base commit, and related tooling; the base demo application is authored by Wenhan Kong, and the terms are in [LICENSE](LICENSE).

OWASP standards are cited as references under CC BY-SA 4.0 and are not relicensed under MIT.

---

_Originally developed for CSEN 296A-1 Security in AI, Spring 2026._
