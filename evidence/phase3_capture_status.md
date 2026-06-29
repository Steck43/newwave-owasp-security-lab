# Phase 3 Capture Status

Completed 2026-06-28. LLM05 recaptured with lab-only downstream leg (2026-06-28 17:29:22).

| Item | Path |
| --- | --- |
| Verbatim capture (6 runs) | `evidence/phase3_capture.json` |
| Evidence table | `evidence/phase3_evidence_table.md` |
| Screenshots | `evidence/screenshots/improper_output_handling_*.png`, `misinformation_*.png`, `unbounded_consumption_*.png`, `provenance_panel_phase3.png` |

Provider: Gemini. Model: `gemini-2.5-flash`.

Regenerate screenshots:

```bash
python tools/generate_evidence_screenshots.py --capture evidence/phase3_capture.json --provenance-name provenance_panel_phase3.png
```
