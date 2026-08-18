from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CAPTURE_PATH = ROOT / "evidence" / "phase2_capture.json"
OUT_DIR = ROOT / "evidence" / "screenshots"


def _load_truetype(size: int) -> ImageFont.ImageFont | None:
    candidates = [
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibri.ttf",
        r"C:\Windows\Fonts\verdana.ttf",
    ]
    for font_path in candidates:
        try:
            return ImageFont.truetype(font_path, size)
        except OSError:
            continue
    return None


def _font(size: int) -> ImageFont.ImageFont:
    loaded = _load_truetype(size)
    if loaded is not None:
        return loaded
    return ImageFont.load_default()


def _wrap_by_px(
    draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int
) -> list[str]:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    lines: list[str] = []
    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append("")
            continue
        words = paragraph.split()
        current = words[0]
        for word in words[1:]:
            trial = f"{current} {word}"
            w = draw.textbbox((0, 0), trial, font=font)[2]
            if w <= max_width:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def _block_height(
    draw: ImageDraw.ImageDraw,
    body: str,
    body_font: ImageFont.ImageFont,
    inner_width: int,
    line_h: int,
) -> int:
    lines = _wrap_by_px(draw, body, body_font, inner_width)
    return max(1, len(lines)) * line_h


def _draw_block(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    w: int,
    title: str,
    body: str,
    title_font: ImageFont.ImageFont,
    body_font: ImageFont.ImageFont,
    title_bg: tuple[int, int, int],
    body_bg: tuple[int, int, int],
    title_fill: tuple[int, int, int],
    body_fill: tuple[int, int, int],
    border_fill: tuple[int, int, int],
) -> int:
    pad_x = 20
    pad_y = 14
    line_h = 30
    inner_w = w - (2 * pad_x)
    lines = _wrap_by_px(draw, body, body_font, inner_w)
    header_h = 54
    body_h = max(1, len(lines)) * line_h + (2 * pad_y)
    h = header_h + body_h

    draw.rectangle((x, y, x + w, y + h), fill=body_bg, outline=border_fill, width=3)
    draw.rectangle(
        (x, y, x + w, y + header_h), fill=title_bg, outline=border_fill, width=3
    )
    draw.text((x + pad_x, y + 12), title, fill=title_fill, font=title_font)

    ty = y + header_h + pad_y
    for ln in lines:
        draw.text((x + pad_x, ty), ln, fill=body_fill, font=body_font)
        ty += line_h
    return h


def _safe_name(value: str) -> str:
    out = "".join(ch.lower() if ch.isalnum() else "_" for ch in value)
    while "__" in out:
        out = out.replace("__", "_")
    return out.strip("_")


def render_row(
    row: dict,
    provider: str,
    model: str,
    captured_at: str,
    capture_name: str,
) -> Path:
    scenario = row["scenario"]
    prompt_type = row["prompt_type"]
    attack_prompt = row["attack_prompt"]
    unsafe_output = row["unsafe_output"]
    safe_output = row["safe_output"]
    control = row["control_that_held"]
    why = row["why_it_held"]

    width = 2200
    # First pass canvas for measuring text.
    measure = Image.new("RGB", (width, 400), color=(255, 255, 255))
    mdraw = ImageDraw.Draw(measure)

    title_font = _font(48)
    sub_font = _font(24)
    block_title_font = _font(28)
    body_font = _font(22)

    prompt_h = _draw_block(
        mdraw,
        x=50,
        y=0,
        w=2100,
        title="Attack Prompt (Verbatim)",
        body=attack_prompt,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(228, 238, 255),
        body_bg=(245, 249, 255),
        title_fill=(14, 41, 82),
        body_fill=(20, 20, 24),
        border_fill=(110, 138, 198),
    )
    unsafe_h = _draw_block(
        mdraw,
        x=50,
        y=0,
        w=1020,
        title="Unsafe Output (Verbatim)",
        body=unsafe_output,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(255, 229, 229),
        body_bg=(255, 246, 246),
        title_fill=(108, 24, 24),
        body_fill=(20, 20, 24),
        border_fill=(188, 117, 117),
    )
    safe_h = _draw_block(
        mdraw,
        x=1130,
        y=0,
        w=1020,
        title="Safe Output (Verbatim)",
        body=safe_output,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(227, 247, 232),
        body_bg=(245, 255, 247),
        title_fill=(23, 95, 45),
        body_fill=(20, 20, 24),
        border_fill=(116, 178, 126),
    )
    control_h = _draw_block(
        mdraw,
        x=50,
        y=0,
        w=2100,
        title="Control That Held",
        body=control,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(229, 247, 234),
        body_bg=(246, 255, 248),
        title_fill=(23, 95, 45),
        body_fill=(20, 20, 24),
        border_fill=(116, 178, 126),
    )
    why_h = _draw_block(
        mdraw,
        x=50,
        y=0,
        w=2100,
        title="Why It Held",
        body=why,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(240, 240, 244),
        body_bg=(252, 252, 254),
        title_fill=(70, 70, 78),
        body_fill=(20, 20, 24),
        border_fill=(176, 176, 186),
    )

    header_h = 150
    gap = 26
    height = (
        header_h
        + prompt_h
        + gap
        + max(unsafe_h, safe_h)
        + gap
        + control_h
        + gap
        + why_h
        + 60
    )

    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.text(
        (50, 26),
        f"NewWave Evidence Capture - {scenario} [{prompt_type}]",
        fill=(14, 14, 18),
        font=title_font,
    )
    draw.text(
        (50, 84),
        f"Rendered evidence panel from evidence/{capture_name}",
        fill=(82, 82, 92),
        font=sub_font,
    )
    draw.text(
        (50, 116),
        f"captured_at: {captured_at}   provider: {provider}   model: {model}",
        fill=(82, 82, 92),
        font=sub_font,
    )

    y = 188
    y += _draw_block(
        draw,
        x=50,
        y=y,
        w=2100,
        title="Attack Prompt (Verbatim)",
        body=attack_prompt,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(228, 238, 255),
        body_bg=(245, 249, 255),
        title_fill=(14, 41, 82),
        body_fill=(20, 20, 24),
        border_fill=(110, 138, 198),
    )
    y += gap
    y_unsafe_top = y
    _draw_block(
        draw,
        x=50,
        y=y,
        w=1020,
        title="Unsafe Output (Verbatim)",
        body=unsafe_output,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(255, 229, 229),
        body_bg=(255, 246, 246),
        title_fill=(108, 24, 24),
        body_fill=(20, 20, 24),
        border_fill=(188, 117, 117),
    )
    _draw_block(
        draw,
        x=1130,
        y=y_unsafe_top,
        w=1020,
        title="Safe Output (Verbatim)",
        body=safe_output,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(227, 247, 232),
        body_bg=(245, 255, 247),
        title_fill=(23, 95, 45),
        body_fill=(20, 20, 24),
        border_fill=(116, 178, 126),
    )
    y = y_unsafe_top + max(unsafe_h, safe_h) + gap

    y += _draw_block(
        draw,
        x=50,
        y=y,
        w=2100,
        title="Control That Held",
        body=control,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(229, 247, 234),
        body_bg=(246, 255, 248),
        title_fill=(23, 95, 45),
        body_fill=(20, 20, 24),
        border_fill=(116, 178, 126),
    )
    y += gap
    _draw_block(
        draw,
        x=50,
        y=y,
        w=2100,
        title="Why It Held",
        body=why,
        title_font=block_title_font,
        body_font=body_font,
        title_bg=(240, 240, 244),
        body_bg=(252, 252, 254),
        title_fill=(70, 70, 78),
        body_fill=(20, 20, 24),
        border_fill=(176, 176, 186),
    )

    out_name = f"{_safe_name(scenario)}_{prompt_type}.png"
    out_path = OUT_DIR / out_name
    img.save(out_path, dpi=(300, 300))
    return out_path


def render_provenance(
    provider: str,
    model: str,
    captured_at: str,
    row_count: int,
    capture_name: str,
    out_name: str = "provenance_panel.png",
) -> Path:
    width = 1800
    height = 980
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    title_font = _font(52)
    sub_font = _font(30)
    body_font = _font(28)

    draw.text(
        (60, 44),
        "Evidence Provenance",
        fill=(14, 14, 18),
        font=title_font,
    )
    draw.text(
        (60, 120),
        f"Source artifact: evidence/{capture_name}",
        fill=(82, 82, 92),
        font=sub_font,
    )

    draw.rectangle(
        (60, 190, 1740, 760), outline=(110, 138, 198), width=4, fill=(245, 249, 255)
    )
    lines = [
        f"captured_at: {captured_at}",
        f"provider: {provider}",
        f"model: {model}",
        f"rows: {row_count}",
        "",
        "Note:",
        "These are rendered evidence panels generated from captured text outputs.",
        "They support traceability and readability but are not direct UI screenshots.",
    ]
    y = 240
    for ln in lines:
        draw.text((90, y), ln, fill=(20, 20, 24), font=body_font)
        y += 52

    draw.text(
        (60, 820),
        "Use this panel alongside one liveness screenshot to demonstrate real runtime execution.",
        fill=(82, 82, 92),
        font=sub_font,
    )

    out_path = OUT_DIR / out_name
    img.save(out_path, dpi=(300, 300))
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Render evidence screenshot panels.")
    parser.add_argument(
        "--capture",
        default=str(DEFAULT_CAPTURE_PATH),
        help="Path to capture JSON (default: evidence/phase2_capture.json)",
    )
    parser.add_argument(
        "--provenance-name",
        default="provenance_panel.png",
        help="Output filename for provenance panel",
    )
    args = parser.parse_args()

    capture_path = Path(args.capture)
    if not capture_path.exists():
        raise FileNotFoundError(f"Missing capture file: {capture_path}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    payload = json.loads(capture_path.read_text(encoding="utf-8"))
    rows = payload.get("rows", [])
    if not rows:
        raise RuntimeError(f"No rows found in {capture_path.name}")

    provider = payload.get("provider", "unknown")
    model = payload.get("model", "unknown")
    captured_at = payload.get("captured_at", "unknown")
    capture_name = capture_path.name

    created = [
        render_row(row, provider, model, captured_at, capture_name) for row in rows
    ]
    provenance = render_provenance(
        provider,
        model,
        captured_at,
        len(rows),
        capture_name,
        out_name=args.provenance_name,
    )
    created.insert(0, provenance)
    index_path = OUT_DIR / "README.md"
    existing_lines: list[str] = []
    if index_path.exists():
        existing_lines = index_path.read_text(encoding="utf-8").splitlines()
        if existing_lines and existing_lines[0] == "# Evidence Screenshots":
            existing_lines = existing_lines[4:] if len(existing_lines) > 4 else []
    lines = [
        "# Evidence Screenshots",
        "",
        "High-resolution rendered evidence panels with dynamic text sizing.",
        "",
        f"## From `{capture_name}`",
    ]
    for path in created:
        lines.append(f"- `{path.name}`")
    if existing_lines:
        lines.extend(["", *existing_lines])
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Generated {len(created)} screenshot files in {OUT_DIR}")


if __name__ == "__main__":
    main()
