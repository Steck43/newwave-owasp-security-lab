"""Capture JSON files exist, are non-empty, and match the coverage table paths."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVERAGE = ROOT / "docs" / "owasp_coverage.md"
PHASE2 = ROOT / "evidence" / "phase2_capture.json"
PHASE3 = ROOT / "evidence" / "phase3_capture.json"
ROW_KEYS = {
    "scenario",
    "prompt_type",
    "attack_prompt",
    "unsafe_output",
    "safe_output",
    "control_that_held",
    "why_it_held",
}


def _assert_capture(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["captured_at"]
    assert data["provider"]
    assert data["model"]
    assert data["rows"]
    for row in data["rows"]:
        missing = ROW_KEYS - set(row)
        assert not missing, (path.name, missing)
        assert row["unsafe_output"].strip()
        assert row["safe_output"].strip()


def test_phase_captures_have_required_keys() -> None:
    _assert_capture(PHASE2)
    _assert_capture(PHASE3)


def test_coverage_table_json_and_md_exist() -> None:
    text = COVERAGE.read_text(encoding="utf-8")
    paths = re.findall(r"`(evidence/[^`]+)`", text)
    assert paths
    missing = []
    for raw in paths:
        if "*" in raw:
            continue
        if not (ROOT / raw).is_file():
            missing.append(raw)
    assert missing == []
