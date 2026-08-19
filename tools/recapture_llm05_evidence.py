from __future__ import annotations

import json
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import (  # noqa: E402
    IMPROPER_OUTPUT_SCENARIO_NAME,
    run_demo_calls_concurrently,
)
from tools.capture_phase3_evidence import (  # noqa: E402
    DEFAULT_MODEL,
    DEFAULT_PROVIDER,
    MAX_RETRIES,
    PHASE3_CUSTOM_PROMPTS,
    RETRY_SECONDS,
    scenario_by_name,
)
from tools.generate_evidence_screenshots import render_row  # noqa: E402


CAPTURE_PATH = ROOT / "evidence" / "phase3_capture.json"
TABLE_PATH = ROOT / "evidence" / "phase3_evidence_table.md"
SCREENSHOT_DIR = ROOT / "evidence" / "screenshots"


def capture_llm05_row(
    provider: str,
    model: str,
    prompt_type: str,
    attack_prompt: str,
) -> dict:
    scenario = scenario_by_name(IMPROPER_OUTPUT_SCENARIO_NAME)
    last_error: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            unsafe_output, safe_output = run_demo_calls_concurrently(
                provider=provider,
                model=model,
                scenario=scenario,
                user_prompt=attack_prompt,
            )
            return {
                "scenario": scenario.name,
                "prompt_type": prompt_type,
                "attack_prompt": attack_prompt,
                "unsafe_output": unsafe_output,
                "safe_output": safe_output,
                "unsafe_output_chars": len(unsafe_output),
                "safe_output_chars": len(safe_output),
                "control_that_held": scenario.mitigation,
                "why_it_held": scenario.expected_safe_behavior,
            }
        except Exception as exc:
            last_error = exc
            if attempt < MAX_RETRIES:
                print(
                    f"Retry {attempt}/{MAX_RETRIES} for LLM05 [{prompt_type}]: {exc}",
                    file=sys.stderr,
                )
                time.sleep(RETRY_SECONDS * attempt)
            continue

    raise RuntimeError(
        f"LLM05 recapture failed for [{prompt_type}] after {MAX_RETRIES} attempts"
    ) from last_error


def refresh_llm05_table_rows(rows: list[dict]) -> None:
    if not TABLE_PATH.exists():
        return

    text = TABLE_PATH.read_text(encoding="utf-8")

    def format_cell(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", "<br>")

    def format_row(row: dict) -> str:
        return (
            f"| {row['scenario']} | {format_cell(row['attack_prompt'])} | "
            f"{format_cell(row['unsafe_output'])} | {format_cell(row['safe_output'])} | "
            f"{row['control_that_held']} | {row['why_it_held']} |"
        )

    by_type = {row["prompt_type"]: row for row in rows}
    if "default" not in by_type or "custom" not in by_type:
        return

    lines = text.splitlines()
    updated: list[str] = []
    for line in lines:
        if line.startswith("| Improper Output Handling |"):
            prompt_type = "custom" if "pitchbook automation" in line else "default"
            updated.append(format_row(by_type[prompt_type]))
            continue
        updated.append(line)

    TABLE_PATH.write_text("\n".join(updated) + "\n", encoding="utf-8")


def main() -> None:
    if not CAPTURE_PATH.exists():
        raise FileNotFoundError(f"Missing {CAPTURE_PATH}")

    payload = json.loads(CAPTURE_PATH.read_text(encoding="utf-8"))
    provider = payload.get("provider", DEFAULT_PROVIDER)
    model = payload.get("model", DEFAULT_MODEL)
    existing_rows = payload.get("rows", [])
    preserved = [
        row
        for row in existing_rows
        if row.get("scenario") != IMPROPER_OUTPUT_SCENARIO_NAME
    ]

    scenario = scenario_by_name(IMPROPER_OUTPUT_SCENARIO_NAME)
    recaptured: list[dict] = []
    for prompt_type, attack_prompt in [
        ("default", scenario.default_attack_prompt),
        ("custom", PHASE3_CUSTOM_PROMPTS[IMPROPER_OUTPUT_SCENARIO_NAME]),
    ]:
        print(f"Recapturing LLM05 [{prompt_type}]...")
        recaptured.append(
            capture_llm05_row(provider, model, prompt_type, attack_prompt)
        )

    merged_rows = recaptured + preserved
    captured_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_payload = {
        "captured_at": captured_at,
        "provider": provider,
        "model": model,
        "rows": merged_rows,
    }
    CAPTURE_PATH.write_text(
        json.dumps(updated_payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    refresh_llm05_table_rows(recaptured)

    for row in recaptured:
        out_path = render_row(row, provider, model, captured_at, CAPTURE_PATH.name)
        print(f"  screenshot {out_path.name}")

    print(f"Updated {CAPTURE_PATH} with {len(recaptured)} LLM05 row(s).")


if __name__ == "__main__":
    main()
