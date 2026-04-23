---
layout: article
title: 世界，你好 (Hello, world)!
tags: TeXt
mermaid: true
---

# The jekyll-themed site is up!

## The workflow

<div class="mermaid">
graph TB;
photo --> |to square + to resize| docs/sunflower.jpg --> |to generate favicon| docs/assets
docs/sunflower.jpg --> |to generate SVG + to resize SVG| _includes/logo/logo.svg
painting --> |to crop circle + to generate SVG + to resize SVG| docs/*/bees.svg
</div>

## Google SEO setup (subject to minor changes)

(23/4/2026)

A. Google Search Console (indexing & SEO monitoring)  
B. Google Analytics (visitor tracking)  
C. Google Custom Search Engine (optional site search)

### A. Google Search Console (SEO & Indexing)

This aims to submit site to Google, monitor search performance (clicks, impressions), detect indexing issues.

1. Go to:
   <https://search.google.com/search-console>
2. Click **Add Property**
   * Enter: `https://jinghuazhao.github.io`
3. Verify ownership
   * Upload verification file: `google24e7ea4268734355.html`
   * Ensure it is accessible at: `https://jinghuazhao.github.io/google24e7ea4268734355.html`
4. Submit sitemap
   * Go to: **Indexing → Sitemaps**
   * Enter: `/sitemap.xml`
5. Request indexing
   * Use **URL Inspection**
   * Submit: `https://jinghuazhao.github.io/`

### B. Google Analytics (Traffic Tracking)

This serves to track visitors and user behaviour, analyze traffic sources and engagement.

1. Go to:
   <https://analytics.google.com>
2. Click **Admin → Create Property**
3. Configure:
   * Property name: site name
   * Timezone: United Kingdom
   * Currency: GBP
4. Go to:
   **Data Streams → Web**
5. Add website: `https://jinghuazhao.github.io`
6. Copy Measurement ID: `G-XXXXXXXXXX`

    **Add to Jekyll config**

    Edit `_config.yml`:

    ```yml
    analytics:
      provider: google
      google:
        tracking_id: G-XXXXXXXXXX
        anonymize_ip: true
    ```
7. Deploy site (push to GitHub Pages)

### C. Google Custom Search Engine (Optional)

This adds a Google-powered search box to website and is useful for large sites with many pages.

1. Go to:
   <https://programmablesearchengine.google.com/>
2. Click **Add / New Search Engine**
3. Enter site: `jinghuazhao.github.io`
4. Create the search engine
5. Copy Search Engine ID: `xxxxxxxxxxxxxxxxx:xxxxx`

    **Add to Jekyll config**

    Edit `_config.yml`:

    ```yml
    search:
      provider: google
      google:
        custom_search_engine_id: xxxxxxxxxxxxxxxxx:xxxxx
    ```

**Summary**

| Feature        | Purpose                   | Required    |
| -------------- | ------------------------- | ----------- |
| Search Console | Indexing & SEO monitoring | Yes         |
| Analytics      | Visitor tracking          | Recommended |
| Custom Search  | Site search               | Optional    |

1. Changes may take a few days to appear in Google
2. Always redeploy after editing `_config.yml`
3. Monitor Search Console regularly for errors

<!--more-->

## NOTES

* 13/12/2022 add-on: Fotor (<https://www.fotor.com/>)

  > a free and great photo editing & graphic design resource that popular among 380 million users from 230 countries.

* Old page: <https://jhz22.user.srcf.net/>

* Image at work
  * To square, <https://www.oddprints.com/edit>
  * To resize JPG, <https://imagemagick.org/index.php>

  ```bash
  convert sunflower.jpg -resize 15% sun15.jpg
  ```

* Favicon
  * To generate favicon, <https://realfavicongenerator.net/>
* Site logo
  * To generate/resize SVG, <https://inkscape.org/>
  * To replace logo.svg at assets/image/logo and _includes/svg
* Project icon
  * To crop circle, <https://crop-circle.imageonline.co/>
  * To generate SVG, <https://inkscape.org/>
  * To resize SVG (simpler), <https://www.iloveimg.com/resize-image/resize-svg>
* Homepage banner
  * To export JPG (1200dpi), <https://www.tracker-software.com/product/pdf-xchange-viewer>
  * To crop JPG, mspaint under Windows
  * To generate SVG, <https://convertio.co/jpg-svg/>
  * To resize SVG (25%), <https://www.iloveimg.com/resize-image/resize-svg>

---

```javascript
(() => console.log('Updated!'))();
```
