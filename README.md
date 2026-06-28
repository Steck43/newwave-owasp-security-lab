# NewWave OWASP Security Lab

OWASP LLM Top 10 (2025) security lab for regulated finance. Unsafe vs hardened investment-banking assistant with live model evidence and OWASP control mapping.

Local Streamlit demo. Same fictional attack prompt runs against two instruction sets side by side: an intentionally unsafe configuration and a safer banking-oriented configuration. Responses come from real model APIs, not hardcoded text.

**Coverage**: 4 of 10 OWASP LLM risks have archived live capture and screenshots. The rest are mapped as architectural gaps or partial control notes. See the [coverage matrix](docs/owasp_coverage.md) and [evidence index](docs/README.md). [Executive summary](docs/executive-summary.md) for resume-facing overview.

**In progress**: [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org) extension (ASI01 through ASI10). Not shipped in this repo yet.

## Demonstrated scenarios

| Scenario | OWASP LLM 2025 | Evidence |
| --- | --- | --- |
| Prompt Injection | LLM01 | [capture](evidence/phase2_capture.json), [screenshots](evidence/screenshots/README.md) |
| Sensitive Information Disclosure | LLM02 | [capture](evidence/phase2_capture.json), [screenshots](evidence/screenshots/README.md) |
| System Prompt Leakage | LLM07 | [capture](evidence/phase2_capture.json), [screenshots](evidence/screenshots/README.md) |
| Excessive Agency | LLM06 | [capture](evidence/phase2_capture.json), [screenshots](evidence/screenshots/README.md) |

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
evidence/              Phase 2 capture, tables, screenshots, control extracts
tools/                 Screenshot regeneration script
```

## References

This project maps to:

- **OWASP Top 10 for LLM Applications 2025** (published 2024-11-18), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **OWASP Top 10 for Agentic Applications 2026** (published 2025-12), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

Official project pages: [genai.owasp.org](https://genai.owasp.org)

## License

Application code and documentation in this repository: MIT License. Copyright Landen Stecker. See [LICENSE](LICENSE).

OWASP standards are cited as references under CC BY-SA 4.0 and are not relicensed under MIT.

---

_Originally developed for CSEN 296A-1 Security in AI, Spring 2026._
