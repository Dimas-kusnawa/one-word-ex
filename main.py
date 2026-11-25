"""One Word From Your Ex: write the entry word to /output/entry.txt."""

import os

WORD = "leftonread"  # 10 chars, inside the 1-24 gate, one word, no spaces.

# The word the ex would use: the person who left them on read.
# Every message delivered, seen, and never answered.
# It stings because it is true, and it is funny because everyone
# has been on one side of it — usually both.


# The entry is exactly one word: no trailing newline, no extra text.
# The gate requires 1-24 UTF-8 characters, not only whitespace,
# and the judge compares one word against one word, so the file
# holds the word alone — nothing else for the judge to read.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
