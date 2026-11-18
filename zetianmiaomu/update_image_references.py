#!/usr/bin/env python3
import csv
import re
from pathlib import Path

ROOT = Path(".")
IMAGE_DIR = ROOT / "assets" / "images"
CSV_FILE = ROOT / "images.csv"

# Build URL-to-local-file mapping using numbered filenames.
with CSV_FILE.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

mapping = {}

for i, row in enumerate(rows, 1):
    url = row["Image URL"].strip()
    matches = list(IMAGE_DIR.glob(f"{i:02d}_*"))

    if not matches:
        print(f"Missing image: {i:02d} {url}")
        continue

    mapping[url] = matches[0]

# Update HTML and CSS, respecting each file's directory.
extensions = {".html", ".htm", ".css"}

for file in ROOT.rglob("*"):
    if file.suffix.lower() not in extensions:
        continue

    if "assets/images" in str(file):
        continue

    text = file.read_text(encoding="utf-8")
    original = text

    for url, image in mapping.items():
        relative = Path(
            __import__("os").path.relpath(image, file.parent)
        ).as_posix()

        text = text.replace(url, relative)

    if text != original:
        file.write_text(text, encoding="utf-8")
        print(f"Updated: {file}")

print(f"\nMapped {len(mapping)} images.")
