"""Documentation build configuration regression tests."""

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def test_docfx_build_includes_install_docs():
    """DocFX content globs should include install docs such as install/uv.md."""
    docfx = json.loads((REPO_ROOT / "docs" / "docfx.json").read_text(encoding="utf-8"))
    content_entries = docfx["build"]["content"]

    all_content_globs = {
        file_glob
        for entry in content_entries
        for file_glob in entry.get("files", [])
    }
    assert "install/*.md" in all_content_globs
