#!/usr/bin/env python3
"""Publish the portable Markdown source as a standard SKILL.md entrypoint."""

from hashlib import sha256
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent
    source = root / "course_study_skill.md"
    target = root / "SKILL.md"
    content = source.read_bytes()
    if not content.startswith(b"---\n"):
        raise SystemExit("Skill source has no YAML frontmatter")
    target.write_bytes(content)
    print(f"SKILL.md synchronized: {sha256(content).hexdigest()}")


if __name__ == "__main__":
    main()
