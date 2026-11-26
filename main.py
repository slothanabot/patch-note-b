#!/usr/bin/env python3
"""make.fun entry: Fix Human Sleep: Funniest Patch Note (patch-note-b).

The entry is one line of patch notes announcing that human sleep
is fixed. The gag reads like a real changelog: a version number, a
terse "fixed", then absurd specs - eight minutes to fall asleep,
dreams in 4K, waking up before the alarm, confused but rested. The
program checks the line against the competition gate (RULES.txt:
/output/entry.txt must be UTF-8 text of 1 to 160 characters, not
only whitespace, a single line) and writes it to /output/entry.txt.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 160


def build_entry():
    """Return the patch-note line, my own wording throughout."""
    # The turn is a software changelog applied to a human body.
    # Sleep gets a version bump and release notes, and the listed
    # "features" are things no update could ever deliver: instant
    # sleep, 4K dreams, and beating the alarm to it.
    return (
        "v2.0.1 - Human sleep: fixed. You now fall asleep in 8 "
        "minutes, dream in 4K, and wake up before the alarm, "
        "confused but rested."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
