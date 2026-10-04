"""Capture JSON files exist, carry required keys, and keep a locked git-blob hash.

Hash the index blob, not the worktree. A Windows checkout can carry CRLF
for a file whose blob is LF. Locking the worktree hash greens the host and
fails every Linux clone — the same class as the atoms SHA256SUMS miss.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVERAGE = ROOT / "docs" / "owasp_coverage.md"
PHASE2 = ROOT / "evidence" / "phase2_capture.json"
PHASE3 = ROOT / "evidence" / "phase3_capture.json"
PHASE2_SHA256 = "71c4f90876121e8c7f88a8a2be89f156d52747933848709d114456698a45f2f0"
PHASE3_SHA256 = "481ea3993236cc3870f645cdc1a481771cfe9ad1135643a8cc344b200a514db4"
ROW_KEYS = {
    "scenario",
    "prompt_type",
    "attack_prompt",
    "unsafe_output",
    "safe_output",
    "control_that_held",
    "why_it_held",
}


def _index_sha256(rel: str) -> str:
    raw = subprocess.check_output(
        ["git", "cat-file", "blob", f":{rel}"],
        cwd=ROOT,
    )
    return hashlib.sha256(raw).hexdigest()


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
    assert _index_sha256("evidence/phase2_capture.json") == PHASE2_SHA256
    assert _index_sha256("evidence/phase3_capture.json") == PHASE3_SHA256


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
