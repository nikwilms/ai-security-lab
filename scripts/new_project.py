"""Create a new project folder from projects/_template.

Usage: python scripts/new_project.py <short-name>
Result: projects/<NNN>-<short-name>/ with the next free number.
"""
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "projects"
TEMPLATE = PROJECTS / "_template"


def main() -> int:
    if len(sys.argv) != 2 or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", sys.argv[1]):
        print("Usage: python scripts/new_project.py <short-name>  (lowercase, digits, dashes)")
        return 1
    name = sys.argv[1]
    numbers = [int(p.name[:3]) for p in PROJECTS.iterdir() if re.match(r"\d{3}-", p.name)]
    number = f"{(max(numbers) + 1) if numbers else 1:03d}"
    target = PROJECTS / f"{number}-{name}"
    shutil.copytree(TEMPLATE, target)
    card = target / "README.md"
    text = card.read_text(encoding="utf-8")
    text = text.replace("<NNN>", number).replace("<title>", name.replace("-", " "))
    text = text.replace("<start>", date.today().isoformat())
    card.write_text(text, encoding="utf-8")
    print(f"Created {target.relative_to(ROOT)}")
    print("Next: fill 01_govern_scope.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
