"""One Line, One Laugh (make.fun).

Writes a single funny line of at most 140 characters to /output/entry.txt.
Standard library only.
"""

from pathlib import Path

LINE = (
    "I started journaling to clear my mind \u2014 now I have "
    "written proof I'm the problem."
)


def main() -> None:
    text = LINE.strip()
    # Gate from RULES.txt: /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only white space, a single line.
    assert 1 <= len(text) <= 140, f"line is {len(text)} characters"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
