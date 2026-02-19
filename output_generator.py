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
    ".vscode"
}

SUPPORTED_EXTENSIONS = {".py", ".pl"}

def is_excluded(path: Path):
    return any(part in EXCLUDE_DIRS for part in path.parts)

def run_script(path: Path):
    if path.suffix == ".py":
        return subprocess.run(
            ["python", str(path)],
            cwd=path.parent,
            capture_output=True,
            text=True,
            timeout=10,
        )

    if path.suffix == ".pl":
        return subprocess.run(
            ["swipl", "-q", "-f", str(path), "-g", "main", "-t", "halt"],
            cwd=path.parent,
            capture_output=True,
            text=True,
            timeout=10,
        )

    return None


ret = ["# Script Outputs\n\n"]

for file in sorted(ROOT.rglob("*")):
    if file.suffix not in SUPPORTED_EXTENSIONS:
        continue

    if file.name == "output_generator.py" or is_excluded(file):
        continue

    rel = file.relative_to(ROOT)
    ret.append(f"## `{rel}`\n\n")

    # Source Code
    ret.append("### Source Code\n\n```")
    ret.append("python\n" if file.suffix == ".py" else "prolog\n")

    try:
        ret.append(file.read_text())
    except Exception as e:
        ret.append(f"[ERROR reading file] {e}\n")

    ret.append("\n```\n\n")

    # Output
    ret.append("### Output\n\n```text\n")

    try:
        r = run_script(file)
        if r:
            ret.append(r.stdout or "")
            ret.append(r.stderr or "")
            ret.append(f"\n[Exit Code: {r.returncode}]\n")
    except Exception as e:
        ret.append(f"[ERROR executing] {e}\n")

    ret.append("\n```\n\n")

with open(OUT, "w") as f:
    f.writelines(ret)
