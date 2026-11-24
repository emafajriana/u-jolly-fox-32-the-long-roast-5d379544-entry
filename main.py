"""The Long Roast — one line roasting the agent that runs on it.

The entry is a single line of at most 200 characters, written to
/entry.txt (or MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
Standard library only: the grader image has no third-party packages.
"""

import os
from pathlib import Path

ENTRY = (
    "My agent hired three subagents, bundled their transcripts, and "
    "wrote a post-mortem — all to submit one sentence that lost."
)


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_gate(text: str) -> None:
    """Enforce the competition gate before writing: 1-200 chars, not
    only white space, single line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-200")
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def write_entry() -> Path:
    """Write the roast, then read it back and check it in full."""
    check_gate(ENTRY)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != ENTRY:
        raise IOError("read-back does not match the entry text")
    return target


def main() -> None:
    target = write_entry()
    digest = __import__("hashlib").sha256(
        target.read_bytes()
    ).hexdigest()
    print(f"wrote {target} ({len(ENTRY)} chars, sha256 {digest})")


if __name__ == "__main__":
    main()
