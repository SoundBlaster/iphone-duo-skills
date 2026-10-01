#!/usr/bin/env python3
"""Validate the plugin manifests and bundled skill structure."""

import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "iphone-duo-examples"
SKILL_FILE = SKILL_DIR / "SKILL.md"
UPSTREAM_URL = "https://github.com/artemnovichkov/iPhone-Duo-by-Examples"


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def load_frontmatter(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", content, re.DOTALL)
    if not match:
        raise ValueError(f"{path.relative_to(ROOT)} has invalid YAML frontmatter")
    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise ValueError("SKILL.md frontmatter must be a YAML mapping")
    return metadata, match.group(2)


def main() -> None:
    portable = load_json(ROOT / "plugin.json")
    codex = load_json(ROOT / ".codex-plugin" / "plugin.json")

    for key in ("name", "version", "description"):
        if portable.get(key) != codex.get(key):
            raise ValueError(f"Plugin manifests disagree on {key!r}")

    if portable.get("name") != "iphone-duo-examples":
        raise ValueError("Unexpected plugin name")
    if codex.get("skills") != "./skills/":
        raise ValueError("Codex manifest must expose ./skills/")
    if not SKILL_FILE.is_file():
        raise ValueError("Bundled iPhone Duo skill is missing")

    metadata, body = load_frontmatter(SKILL_FILE)
    if metadata.get("name") != SKILL_DIR.name:
        raise ValueError("Skill name must match its directory name")
    if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
        raise ValueError("Skill description is missing")
    if UPSTREAM_URL not in body:
        raise ValueError("Skill must reference the upstream iPhone Duo examples repository")

    layout_reference = SKILL_DIR / "references" / "adaptive-layout-lessons.md"
    if not layout_reference.is_file():
        raise ValueError("Linked adaptive layout reference is missing")
    if "[adaptive layout lessons](references/adaptive-layout-lessons.md)" not in body:
        raise ValueError("SKILL.md must link the adaptive layout reference")

    interface_file = SKILL_DIR / "agents" / "openai.yaml"
    if not interface_file.is_file() or not isinstance(
        yaml.safe_load(interface_file.read_text(encoding="utf-8")), dict
    ):
        raise ValueError("Skill OpenAI interface metadata must be a YAML mapping")

    print("Plugin manifests and bundled skill structure are valid.")


if __name__ == "__main__":
    main()
