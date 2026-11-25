"""Entry: one Wi-Fi network name, at most 32 characters.

The gate checks /output/entry.txt is UTF-8 text of 1 to 32 characters, not only whitespace. The name is written with no trailing newline so the file holds exactly the name and nothing else.
"""

import os

NAME = "Monk Breaks Silence: Soup's Cold"


def main() -> None:
    if not (1 <= len(NAME) <= 32) or not NAME.strip():
        raise ValueError(
            f"NAME must be non-empty and between 1 and 32 characters long. Got length {len(NAME)}."
        )

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, "entry.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(NAME)

    print(f"Wrote to {file_path} ({len(NAME)} characters)")


if __name__ == "__main__":
    main()
