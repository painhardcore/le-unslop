"""Check punctuation spacing in plain France French prose, without changing it."""

import argparse
from pathlib import Path
import re


BAD_SPACING = re.compile(r"(?<![\u00a0\u202f])[:;!?»]|«(?![\u00a0\u202f])")


def spacing_errors(text):
    for line_number, line in enumerate(text.splitlines(), 1):
        for match in BAD_SPACING.finditer(line):
            yield line_number, match.start() + 1, match.group()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="UTF-8 prose excerpt without technical literals")
    args = parser.parse_args()
    try:
        text = args.file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        parser.exit(2, f"{args.file}: {error}\n")
    errors = list(spacing_errors(text))
    for line, column, symbol in errors:
        print(f"{args.file}:{line}:{column}: expected non-breaking space beside {symbol!r}")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
