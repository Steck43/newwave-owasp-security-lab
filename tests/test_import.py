"""Smoke import so the floor tests job has a real collection."""

from __future__ import annotations

import app


def test_app_module_loads() -> None:
    assert app.PROVIDERS
