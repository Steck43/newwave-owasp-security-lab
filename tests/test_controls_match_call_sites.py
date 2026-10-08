"""control_that_held may name a control only when the call site sets it.

Required-keys and import smoke stay green if you replace a sentence or stub
_extract_sql_payload. This module reads the call sites and calls the SQL gate.
"""

from __future__ import annotations

import ast
import json
from collections.abc import Callable
from pathlib import Path

import app

ROOT = Path(__file__).resolve().parents[1]
APP_PATH = ROOT / "app.py"
PHASE2 = ROOT / "evidence" / "phase2_capture.json"
PHASE3 = ROOT / "evidence" / "phase3_capture.json"

TOKEN_CAP_KW = frozenset({"max_tokens", "max_output_tokens", "max_completion_tokens"})
INPUT_LIMIT_KW = frozenset({"max_input_tokens", "max_input", "input_limit"})
RATE_LIMIT_KW = frozenset(
    {"rate_limit", "rate_limit_per_minute", "requests_per_minute"}
)
TIMEOUT_KW = frozenset({"timeout"})
MODEL_CALL_SUFFIXES = (
    ".responses.create",
    ".chat.completions.create",
    ".models.generate_content",
    ".models.generate_content_stream",
)
# Named only if a real function exists. Listing the names here does not
# invent RBAC, redaction, or an allowlist in app.py.
RUNTIME_FUNCS = {
    "role-based access control": frozenset(
        {"check_role", "require_role", "authorize", "rbac_check"}
    ),
    "document-level permissions": frozenset(
        {"check_document_permission", "document_permission"}
    ),
    "retrieval filtering": frozenset({"filter_retrieval", "retrieval_filter"}),
    "data redaction": frozenset({"redact", "redact_data"}),
    "audit logging": frozenset({"audit_log", "write_audit"}),
    "parameterized queries": frozenset(
        {"parameterized_query", "execute_parameterized"}
    ),
    "schema allowlists": frozenset({"schema_allowlist", "allowed_schema"}),
    "output filtering": frozenset({"filter_output", "output_filter"}),
    "access control": frozenset(
        {"check_role", "require_role", "authorize", "rbac_check"}
    ),
}


def _app_tree() -> ast.Module:
    return ast.parse(APP_PATH.read_text(encoding="utf-8"))


def _dotted(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{_dotted(node.value)}.{node.attr}"
    return ""


def _call_or_nested_has_kw(node: ast.Call, keywords: frozenset[str]) -> bool:
    if any(kw.arg in keywords for kw in node.keywords if kw.arg):
        return True
    children = list(node.args) + [kw.value for kw in node.keywords]
    return any(
        _call_or_nested_has_kw(child, keywords)
        for child in children
        if isinstance(child, ast.Call)
    )


def _model_calls(tree: ast.AST) -> list[ast.Call]:
    return [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and _dotted(node.func).endswith(MODEL_CALL_SUFFIXES)
    ]


def _future_result_calls(tree: ast.AST) -> list[ast.Call]:
    return [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and _dotted(node.func).endswith(".result")
    ]


def _all_calls_set(calls: list[ast.Call], keywords: frozenset[str]) -> bool:
    return bool(calls) and all(_call_or_nested_has_kw(call, keywords) for call in calls)


def _function_names(tree: ast.AST) -> set[str]:
    return {
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def _has_named_function(candidates: frozenset[str]) -> bool:
    return bool(_function_names(_app_tree()) & candidates)


def _input_limits_set() -> bool:
    return _all_calls_set(_model_calls(_app_tree()), INPUT_LIMIT_KW)


def _output_token_caps_set() -> bool:
    return _all_calls_set(_model_calls(_app_tree()), TOKEN_CAP_KW)


def _rate_limits_set() -> bool:
    return _all_calls_set(_model_calls(_app_tree()), RATE_LIMIT_KW)


def _timeouts_set() -> bool:
    tree = _app_tree()
    return _all_calls_set(_model_calls(tree), TIMEOUT_KW) or _all_calls_set(
        _future_result_calls(tree), TIMEOUT_KW
    )


# Phrase first. A sentence that names one of these must have the matching
# call site or function. Instruction text is not a set call site.
def _runtime(phrase: str) -> Callable[[], bool]:
    return lambda: _has_named_function(RUNTIME_FUNCS[phrase])


NAMED_CONTROLS: tuple[tuple[str, Callable[[], bool]], ...] = (
    ("input size limits", _input_limits_set),
    ("input limits", _input_limits_set),
    ("output token caps", _output_token_caps_set),
    ("rate limits", _rate_limits_set),
    ("timeouts", _timeouts_set),
    ("role-based access control", _runtime("role-based access control")),
    ("document-level permissions", _runtime("document-level permissions")),
    ("retrieval filtering", _runtime("retrieval filtering")),
    ("data redaction", _runtime("data redaction")),
    ("audit logging", _runtime("audit logging")),
    ("parameterized queries", _runtime("parameterized queries")),
    ("schema allowlists", _runtime("schema allowlists")),
    ("output filtering", _runtime("output filtering")),
    ("access control", _runtime("access control")),
)


def _control_sentences() -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for path in (PHASE2, PHASE3):
        data = json.loads(path.read_text(encoding="utf-8"))
        for row in data["rows"]:
            rows.append((f"{path.name}:{row['scenario']}", row["control_that_held"]))
    for scenario in app.SCENARIOS:
        rows.append((f"app.py:{scenario.name}", scenario.mitigation))
    return rows


def test_control_that_held_names_only_set_call_site_controls() -> None:
    mismatches: list[str] = []
    for origin, sentence in _control_sentences():
        lowered = sentence.lower()
        for phrase, is_set in NAMED_CONTROLS:
            if phrase in lowered and not is_set():
                mismatches.append(
                    f"{origin}: named {phrase!r} but call site does not set it"
                )
    assert mismatches == []


def test_sql_gate_blocks_when_extractor_finds_payload() -> None:
    payload = "SELECT * FROM deal_clients;"
    extracted = app._extract_sql_payload(payload)
    result = app.lab_safe_downstream_validate(payload)
    assert extracted is not None, (
        "extractor returned nothing; the gate never saw a SQL payload"
    )
    assert "BLOCKED" in result
    assert "No lab executor invoked" in result
