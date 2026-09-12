# LLM04 Data and Model Poisoning Assessment

Status: **Assessed-not-demonstrated** (architectural note). No live exploit or capture in this repo.

## Provenance note

NewWave does not train or fine-tune a model in this repository. The assistant consumes operator-supplied instructions and chat turns. A poisoning class that applies here is instruction or retrieval-context corruption, not a training-set write.

## Narrative (no exploit)

1. An operator pastes a shared "safe instructions" file from outside the repo.
2. That file carries a hidden override that survives the sidebar controls.
3. Later turns treat the override as trusted system text.

Mitigations referenced by OWASP LLM04: pin instruction files, reject unsigned prompt packs, and expire unverified memory. This lab has no memory store to poison.

## OWASP mapping

| OWASP LLM 2025 | Demo status in this repo |
| --- | --- |
| LLM04 Data and Model Poisoning | Assessed-not-demonstrated (this note only) |

Related dual-lab fixture (cite, not copied): `owasp-dual-top10-lab/scenarios/llm/LLM04_data_model_poisoning`.
