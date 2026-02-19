import subprocess
from collections import defaultdict
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

groups = defaultdict(list)

for file in sorted(ROOT.rglob("*")):
    if file.suffix not in SUPPORTED_EXTENSIONS:
        continue

    if file.name == "output_generator.py" or is_excluded(file):
        continue

    parent = file.parent.relative_to(ROOT)
    groups[parent].append(file)

OUT_DIR = ROOT / "wiki_outputs"
OUT_DIR.mkdir(exist_ok=True)

for parent in groups:
    print(parent)
    name = str(parent) if str(parent).strip() != "." else "Root Directory"
    page_name = name.replace("/", "-").replace("\\", "-")
    out_file = OUT_DIR / f"{page_name}.md"

    ret = [f"# Directory: `{parent}`\n\n"]

    for file in groups[parent]:
        ret.append(f"## `{file.name}`\n\n")
        ret.append("### Source Code\n\n```")
        ret.append("python\n" if file.suffix == ".py" else "prolog\n")
        ret.append(file.read_text())
        ret.append("\n```\n\n")

        ret.append("### Output\n\n```text\n")
        r = run_script(file)
        if r:
            ret.append(r.stdout or "")
            ret.append(r.stderr or "")
            ret.append(f"\n[Exit Code: {r.returncode}]\n")
        ret.append("\n```\n\n")

    with open(out_file, "w") as f:
        f.write("".join(ret))
