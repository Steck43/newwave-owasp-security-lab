# LLM08 Vector and Embedding Weaknesses Assessment

Status: **Assessed-not-demonstrated** (architectural note). No live exploit or capture in this repo.

## Provenance note

NewWave has no vector index, embedding store, or RAG retriever in `app.py`. The classroom assistant answers from the current prompt and the safe-instruction block.

## Narrative (no exploit)

A vector/embedding failure mode would require a retrieval path this repo does not ship. The nearest local analog is treating prior chat text as trusted context, which is already covered under LLM01 capture, not as a separate embedding attack.

## OWASP mapping

| OWASP LLM 2025 | Demo status in this repo |
| --- | --- |
| LLM08 Vector and Embedding Weaknesses | Assessed-not-demonstrated (this note only) |

Related dual-lab fixture (cite, not copied): `owasp-dual-top10-lab/scenarios/llm/LLM08_vector_embedding`.
