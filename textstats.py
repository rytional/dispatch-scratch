"""Tiny text statistics CLI used to exercise Dispatch (diffs, test runs, command output).

Usage:
    python3 textstats.py FILE [--top N]
    echo "some text" | python3 textstats.py - --top 3
"""

import argparse
import re
import sys
from collections import Counter

WORD_RE = re.compile(r"[A-Za-z0-9']+")


def words(text):
    """Return lowercase words found in text."""
    return [w.lower() for w in WORD_RE.findall(text)]


def stats(text, top=5):
    """Return a dict of basic statistics for text."""
    ws = words(text)
    return {
        "lines": len(text.splitlines()),
        "words": len(ws),
        "chars": len(text),
        "unique_words": len(set(ws)),
        "top_words": Counter(ws).most_common(top),
    }


def format_stats(result):
    """Render a stats dict as aligned plain text."""
    out = [
        f"lines:        {result['lines']}",
        f"words:        {result['words']}",
        f"chars:        {result['chars']}",
        f"unique words: {result['unique_words']}",
        "top words:",
    ]
    out += [f"  {count:>4}  {word}" for word, count in result["top_words"]]
    return "\n".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("file", help="path to a text file, or - for stdin")
    parser.add_argument("--top", type=int, default=5, help="number of top words to show")
    args = parser.parse_args(argv)

    if args.file == "-":
        text = sys.stdin.read()
    else:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()

    print(format_stats(stats(text, args.top)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
