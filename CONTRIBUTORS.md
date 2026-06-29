# Contributors

## Wenhan Kong

Base NewWave Deal Assistant Streamlit demo introduced in commit `cda59f1` (`Build NewWave LLM security Streamlit demo`, 2026-05-26).

Wenhan authored the initial `app.py`, `.env.example`, `.gitignore`, `requirements.txt`, and course README. That base includes:

- Four classroom scenarios: Prompt Injection (LLM01), Sensitive Information Disclosure (LLM02), System Prompt Leakage (LLM07), and Excessive Agency (LLM06)
- Core unsafe and safe assistant instruction blocks
- Tagged input harness (`build_llm_input`, `<fictional_context>` / `<user_attack_prompt>`)
- Parallel unsafe vs safe demo execution and Streamlit UI
- OpenAI, Gemini, and OpenRouter provider integration

## Landen Stecker (Steck43)

Security assessment, portfolio repackage, and evidence on branch `repackage-owasp-lab` (commits after `cda59f1`).

Landen added or authored:

- OWASP LLM Top 10 (2025) coverage matrix, executive summary, scope and limitations, and related documentation
- MITRE ATLAS and NIST AI RMF alignment in docs
- Phase 2 and Phase 3 evidence capture (`evidence/phase2_capture.json`, `evidence/phase3_capture.json`), evidence tables, screenshots, and control-mapping artifacts
- Three additional scenarios: Improper Output Handling (LLM05), Misinformation (LLM09), and Unbounded Consumption (LLM10)
- Safe and unsafe instruction lines for LLM05, LLM09, and LLM10 behavior
- Lab-only LLM05 downstream executor and validation gate (`finalize_demo_responses` and related helpers)
- Capture and screenshot tooling under `tools/`
- LLM03 supply-chain architectural assessment note
- Portfolio README reframe and repository `LICENSE` file

Landen did not author the original four scenarios or the base Streamlit harness in `cda59f1`.
