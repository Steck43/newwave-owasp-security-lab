# Phase 3 Capture Status

Phase 3 scenarios are implemented in `app.py` and the capture script is at `tools/capture_phase3_evidence.py`.

**Capture not completed.** `python tools/capture_phase3_evidence.py` failed on 2026-06-28 with `API_KEY_INVALID` for `GEMINI_API_KEY`. No `phase3_capture.json` was written. Do not mark LLM05, LLM09, or LLM10 as Demonstrated until a valid capture run finishes.

To capture after fixing the key:

```bash
python tools/capture_phase3_evidence.py
python tools/generate_evidence_screenshots.py --capture evidence/phase3_capture.json --provenance-name provenance_panel_phase3.png
```

Then regenerate `evidence/phase3_evidence_table.md` and update coverage docs to seven Demonstrated risks.
