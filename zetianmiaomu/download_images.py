
#!/usr/bin/env python3
"""Download images listed in a CSV file and preserve their metadata."""

import csv
import re
import mimetypes
import time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlparse, unquote

INPUT_CSV = Path("images.csv")
OUTPUT_DIR = Path("downloaded_images")
OUTPUT_CSV = Path("images_downloaded.csv")

TIMEOUT = 60
DELAY = 0.5


def slug(text):
    """Create a filesystem-safe filename component."""
    text = unquote(str(text or ""))
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", text)
    text = re.sub(r"\s+", "_", text.strip())
    return text[:70].strip("._") or "image"


def download_image(url, destination):
    """Download an image and determine its file extension."""
    request = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; ImageDownloader/1.0)"}
    )

    with urlopen(request, timeout=TIMEOUT) as response:
        content_type = response.headers.get_content_type()
        data = response.read()

    extension = mimetypes.guess_extension(content_type) or ".jpg"

    # Prefer the extension supplied by the URL when available.
    url_extension = Path(urlparse(url).path).suffix.lower()
    if url_extension in (".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"):
        extension = url_extension

    destination = destination.with_suffix(extension)
    destination.write_bytes(data)

    return destination


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with INPUT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        required = {"Page", "Section", "Section title",
                    "Location", "Image URL", "Source", "Attribution"}

        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing CSV columns: {', '.join(missing)}")

        rows = list(reader)

    results = []

    for i, row in enumerate(rows, start=1):
        url = row["Image URL"].strip()

        page = slug(row["Page"])
        section = slug(row["Section"])
        location = slug(row["Location"])

        filename = f"{i:02d}_{page}_{section}_{location}"

        print(f"[{i}/{len(rows)}] {filename}")

        try:
            if not url:
                raise ValueError("Missing image URL")

            path = download_image(url, OUTPUT_DIR / filename)

            row["Local file"] = str(path)
            row["Download status"] = "OK"
            row["Error"] = ""

            print(f"  Downloaded: {path}")

        except Exception as e:
            row["Local file"] = ""
            row["Download status"] = "FAILED"
            row["Error"] = str(e)

            print(f"  FAILED: {e}")

        results.append(row)
        time.sleep(DELAY)

    columns = list(rows[0].keys()) if rows else []
    columns += ["Local file", "Download status", "Error"]

    with OUTPUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(results)

    successful = sum(
        r["Download status"] == "OK" for r in results
    )

    print("\nDownload summary")
    print("----------------")
    print(f"Total:      {len(results)}")
    print(f"Successful: {successful}")
    print(f"Failed:     {len(results) - successful}")
    print(f"Images:     {OUTPUT_DIR.resolve()}")
    print(f"Manifest:   {OUTPUT_CSV.resolve()}")


if __name__ == "__main__":
    main()
