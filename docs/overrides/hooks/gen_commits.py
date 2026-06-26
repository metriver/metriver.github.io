"""
MkDocs hook: generate commits.json with daily git commit counts.
Runs during build → writes to docs/commits.json → gets copied to site/.
"""
import subprocess, json, os
from datetime import datetime

def on_pre_build(config):
    docs_dir = config.docs_dir
    out = os.path.join(docs_dir, "commits.json")
    try:
        result = subprocess.run(
            ["git", "log", "--format=%ad", "--date=short", "--since=90.days"],
            capture_output=True, text=True, cwd=docs_dir, timeout=10,
        )
        counts = {}
        for line in result.stdout.strip().splitlines():
            d = line.strip()
            if d:
                counts[d] = counts.get(d, 0) + 1
        with open(out, "w") as f:
            json.dump(counts, f)
    except Exception:
        # git not available (e.g. shallow clone) — write empty, frontend falls back
        with open(out, "w") as f:
            json.dump({}, f)
