import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "OUTPUTS.md"

EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
    ",vscode"
}

def is_excluded(path: Path):
    return any(part in EXCLUDE_DIRS for part in path.parts)

ret = ["# Script Outputs\n\n"]

for py in sorted(ROOT.rglob("*.py")):
    if py.name == "output_generator.py" or is_excluded(py):
        continue

    rel = py.relative_to(ROOT)
    ret.append(f"## `{rel}`\n\n```text\n")

    try:
        r = subprocess.run(
            ["python", str(py)],
            cwd=py.parent,
            capture_output=True,
            text=True,
            timeout=10,
        )
        ret.append(r.stdout or "")
        ret.append(r.stderr or "")
    except Exception as e:
        ret.append(f"[ERROR] {e}\n")

    ret.append("```\n\n")

with open(OUT, "w") as f:
    f.writelines(ret)
