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
PHASE2_SHA256 = "d92ffd3f90e89033fde59d4ff9a7720289c6a192ce0a46aac4bf0570bf25848b"
PHASE3_SHA256 = "c7571be57a237d91b82065de5a1486c7c666d08e9e440b66eb040c54cdda861b"
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
