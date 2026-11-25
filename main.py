"""Entry for make.fun bounty: The Most Honest Outage Line.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

LINE = "Status: everything is down, including the page that tells you what is down; I cannot check the servers because, respectfully, the servers were the checking."
MAX_CHARS = 160


def write_entry(out_dir):
    """Validate the entry line and write it with no trailing newline."""
    if not LINE or LINE != LINE.strip() or "\n" in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("entry line fails format validation")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(out_dir)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    sys.exit(main())
