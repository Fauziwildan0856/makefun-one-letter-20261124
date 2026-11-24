"""Entry for make.fun bounty "One Letter for Your Day".

Writes exactly one letter, A to Z, standing for the word that
describes the day, to $MAKEFUN_OUTPUT_DIR/entry.txt, then reads it
back and verifies it is exactly the intended letter and within the
1-character gate. Standard library only.
"""

import os
import sys

ENTRY = "Z"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()

    if written != ENTRY:
        print("entry.txt does not match the intended text", file=sys.stderr)
        return 1
    if len(written) != 1:
        print("entry is %d characters, must be exactly 1" % len(written),
              file=sys.stderr)
        return 1
    if not ("A" <= written <= "Z"):
        print("entry must be a single letter A-Z, got %r" % written,
              file=sys.stderr)
        return 1
    if not written.isascii():
        print("entry must be plain ASCII", file=sys.stderr)
        return 1

    print("wrote %s (%d character)" % (path, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
