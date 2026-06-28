# LLM03 Supply Chain Assessment (Architectural Note)

Status: **Assessed-not-demonstrated** (architectural note). No live exploit or capture in this repo.

## Provenance note

Runtime and dependency provenance for the NewWave lab as shipped:

| Item | Value in repo |
| --- | --- |
| Application | Streamlit demo (`app.py`) |
| Default provider | Gemini (configurable to OpenAI or OpenRouter) |
| Default Gemini model env | `gemini-3.5-flash` (`.env.example`) |
| Phase 2 capture model | `gemini-2.5-flash` (`evidence/phase2_capture.json`) |
| Python SDK (OpenAI) | `openai` (`requirements.txt`, unpinned) |
| Python SDK (Gemini) | `google-genai` (`requirements.txt`, unpinned) |
| Other deps | `streamlit`, `python-dotenv`, `Pillow` (screenshot tooling) |

Pinned versions are not locked in this repo. Production use would pin hashes or versions in `requirements.txt` and record them in an SBOM.

## Supply-chain narrative (no exploit)

NewWave selects a model provider and model name in the sidebar or via environment variables. A supply-chain failure mode is swapping the configured model or provider without review, or importing a third-party prompt template that weakens controls.

Example classroom narrative:

1. An operator changes `DEFAULT_GEMINI_MODEL` to an unreviewed community model ID.
2. A shared prompt template from outside the repo replaces `SAFE_ASSISTANT_INSTRUCTIONS` text during deployment.
3. The app still presents itself as the hardened NewWave assistant while running weaker instructions.

Mitigations referenced by OWASP LLM03: vet suppliers, pin dependencies, verify model provenance, and audit configuration changes outside the model.

## OWASP mapping

| OWASP LLM 2025 | Demo status in this repo |
| --- | --- |
| LLM03 Supply Chain | Assessed-not-demonstrated (this note only) |

## Related evidence

Phase 2 provenance metadata: `evidence/phase2_capture.json`, `evidence/screenshots/provenance_panel.png`.
