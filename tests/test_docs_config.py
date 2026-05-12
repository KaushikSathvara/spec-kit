"""Documentation build configuration regression tests."""

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def test_docfx_build_includes_install_docs():
    """DocFX content globs should include install docs such as install/uv.md."""
    docfx = json.loads((REPO_ROOT / "docs" / "docfx.json").read_text(encoding="utf-8"))
    content_entries = docfx["build"]["content"]

    root_content = next(
        entry for entry in content_entries if "toc.yml" in entry.get("files", [])
    )
    assert "install/*.md" in root_content["files"]
