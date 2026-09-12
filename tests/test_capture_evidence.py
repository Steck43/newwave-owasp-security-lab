"""Capture JSON files exist, carry required keys, and keep a locked content hash."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVERAGE = ROOT / "docs" / "owasp_coverage.md"
PHASE2 = ROOT / "evidence" / "phase2_capture.json"
PHASE3 = ROOT / "evidence" / "phase3_capture.json"
PHASE2_SHA256 = "6e83a7067b2f016d490f6f2fe04198140caf1292a5fabb708a17088f2992e888"
PHASE3_SHA256 = "b5d57318f75e64ae7331ea914bd42cf53ed48cf0d4c1cdddb2eb3e35b106d73a"
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


def test_phase_captures_keep_locked_hash() -> None:
    assert hashlib.sha256(PHASE2.read_bytes()).hexdigest() == PHASE2_SHA256
    assert hashlib.sha256(PHASE3.read_bytes()).hexdigest() == PHASE3_SHA256


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
