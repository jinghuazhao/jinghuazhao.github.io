#!/usr/bin/env python3
"""Make a Soloist export more portable for GitHub Pages.

Usage:
  python migrate_solo_site.py solo-websites-20261118203431.zip \
      --images downloaded_images --output ~/tests/zetianmiaomu

The script preserves the exported layout, copies the 16 downloaded images,
rewrites Solo/Unsplash image URLs to local files, fixes canonical URLs and
normalises the known double-slash video path. It does not invent a backend
for contact/newsletter forms or replace the map placeholder.
"""
from __future__ import annotations
import argparse, csv, re, shutil, zipfile
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_SITE_URL = "https://jinghuazhao.github.io/tests/zetianmiaomu"
# The downloader's numbered files correspond to images.csv rows in this order.
IMAGE_NAMES = [
    "hero.jpg", "hero-background.jpg",
    "service-disease-control.jpg", "service-cultivation.jpg",
    "service-sustainability.jpg", "service-exhibition.jpg",
    "gallery-01.jpg", "gallery-02.jpg", "gallery-03.jpg",
    "gallery-04.jpg", "gallery-05.jpg", "gallery-06.jpg",
    "banner.jpg", "blog-cherry-planting.jpg",
    "blog-cultivation-trends.jpg", "blog-nursery-day.jpg",
]


def numbered_images(folder: Path) -> list[Path]:
    files = sorted(p for p in folder.iterdir() if p.is_file() and re.match(r"^\d{2}_", p.name))
    if len(files) < 16:
        raise SystemExit(f"Expected 16 numbered downloaded images in {folder}; found {len(files)}")
    return files[:16]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("archive", type=Path, help="Solo export ZIP")
    ap.add_argument("--images", type=Path, default=Path("downloaded_images"), help="Folder containing 01_... through 16_... images")
    ap.add_argument("--output", type=Path, default=Path("~/tests/zetianmiaomu"), help="Output website directory (default: ~/tests/zetianmiaomu)")
    ap.add_argument("--site-url", default=DEFAULT_SITE_URL, help="Public URL used for canonical/metadata links")
    args = ap.parse_args()
    args.output = args.output.expanduser().resolve()
    site_url = args.site_url.rstrip("/")
    if not args.archive.is_file(): raise SystemExit(f"ZIP not found: {args.archive}")
    if not args.images.is_dir(): raise SystemExit(f"Image folder not found: {args.images}")
    if args.output.exists(): raise SystemExit(f"Output already exists; move/delete it first: {args.output}")

    with zipfile.ZipFile(args.archive) as z:
        roots = {Path(n).parts[0] for n in z.namelist() if n and not n.startswith("__MACOSX/")}
        if len(roots) != 1: raise SystemExit(f"Expected one top-level folder in ZIP; found {sorted(roots)}")
        z.extractall(args.output.parent)
        extracted = args.output.parent / next(iter(roots))
        shutil.move(str(extracted), str(args.output))

    image_dir = args.output / "assets" / "images"
    image_dir.mkdir(parents=True, exist_ok=True)
    sources = numbered_images(args.images)
    mapping: dict[str, str] = {}
    for src, name in zip(sources, IMAGE_NAMES):
        dest = image_dir / name
        shutil.copy2(src, dest)
        mapping[src.name] = name

    # Read exported image manifest: UUIDs identify the 13 Solo images and
    # the three Unsplash photo IDs identify the blog cover images.
    manifest = args.output / "images.csv"
    solo_id_to_name: dict[str, str] = {}
    unsplash_id_to_name: dict[str, str] = {}
    if manifest.exists():
        with manifest.open(encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        for i, row in enumerate(rows[:16]):
            url = row.get("Image URL", "")
            if "cdn.soloist.ai" in url:
                m = re.search(r"/([0-9a-f-]{36})\.jpg", url, re.I)
                if m: solo_id_to_name[m.group(1).lower()] = IMAGE_NAMES[i]
            elif "images.unsplash.com" in url:
                m = re.search(r"/photo-([0-9]+-[A-Za-z0-9-]+)", url)
                if m: unsplash_id_to_name[m.group(1)] = IMAGE_NAMES[i]

    changed = []
    unresolved = set()
    # Rewrite HTML and CSS URLs, preserving relative paths from each page.
    for file in list(args.output.rglob("*.html")) + list(args.output.rglob("*.css")):
        text = file.read_text(encoding="utf-8", errors="replace")
        original = text
        rel_prefix = "../" * len(file.relative_to(args.output).parent.parts)
        def local_for_url(url: str) -> str | None:
            parsed = urlparse(url.replace("&amp;", "&"))
            if "cdn.soloist.ai" in parsed.netloc:
                m = re.search(r"/([0-9a-f-]{36})_\d+x\d+\.webp$|/([0-9a-f-]{36})\.jpg$", parsed.path, re.I)
                if m:
                    ident = (m.group(1) or m.group(2)).lower()
                    name = solo_id_to_name.get(ident)
                    if name: return rel_prefix + "assets/images/" + name
            if "images.unsplash.com" in parsed.netloc:
                m = re.search(r"/photo-([0-9]+-[A-Za-z0-9-]+)", parsed.path)
                if m:
                    name = unsplash_id_to_name.get(m.group(1))
                    if name: return rel_prefix + "assets/images/" + name
            return None
        # Replace quoted URL strings, including URLs in inline CSS.
        url_re = re.compile(r"https?://(?:cdn\.soloist\.ai|images\.unsplash\.com)/[^\"'\s)<>]+")
        def replace_url(match):
            url = match.group(0)
            local = local_for_url(url)
            if local: return local
            unresolved.add(url[:180])
            return url
        text = url_re.sub(replace_url, text)
        # Site canonical/OG URLs should point to the GitHub Pages project site.
        text = text.replace("https://soloist.ai/favicon/favicon.ico", "")
        text = text.replace("https://soloist.ai/zetianmiaomu", site_url)
        text = text.replace("https://soloist.ai/", site_url + "/")
        # Correct accidental double slash in known video paths.
        text = text.replace("/tests//ztmm/", "/tests/ztmm/")
        if text != original:
            file.write_text(text, encoding="utf-8")
            changed.append(str(file.relative_to(args.output)))

    # Remove stale CSVs from the public website; retain them in the original ZIP.
    for name in ("images.csv", "contacts.csv"):
        p = args.output / name
        if p.exists(): p.unlink()

    report = args.output / "MIGRATION-REPORT.txt"
    report.write_text(
        "Solo export migration report\n"
        f"Site URL: {site_url}/\n"
        f"Images copied: {len(sources)}\n"
        f"HTML/CSS files changed: {len(changed)}\n"
        "\nStill requiring manual review:\n"
        "- Contact/newsletter controls have no submission backend in the static export.\n"
        "- The map section is a placeholder; add an Amap link or independent embed.\n"
        "- Check all video URLs and every page in a browser.\n"
        "- Google Fonts remains an external font dependency.\n"
        "- Any unresolved external image URLs listed below need attention.\n\n"
        + "\n".join(sorted(unresolved)) + "\n",
        encoding="utf-8")
    print(f"Created: {args.output.resolve()}")
    print(f"Copied {len(sources)} images; updated {len(changed)} HTML/CSS files.")
    print(f"Review: {report}")
    if unresolved: print(f"WARNING: {len(unresolved)} external image URL(s) were not mapped; see report.")
    else: print("All recognised Solo/Unsplash image URLs were mapped to local files.")
    print("Test locally from the output directory with: python -m http.server 8000")

if __name__ == "__main__": main()
