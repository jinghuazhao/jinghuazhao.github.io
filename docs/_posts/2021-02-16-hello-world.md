---
layout: article
title: Hello, world!
tags: info
mathjax: true
mathjax_autoNumber: false
mermaid: true
---

# The jekyll-themed site is up!

<!--more-->

# NOTES

* Old page: [https://jhz22.user.srcf.net/](https://jhz22.user.srcf.net/)

**English title than smaller title image**

The workflow to set up
```
graph TB;
photo --> |to square + to resize| docs/sunflower.jpg --> |to generate favicon| docs/assets
docs/sunflower.jpg --> |to generate SVG + to resize SVG| _includes/logo/logo.svg
painting --> |to crop circle + to generate SVG + to resize SVG| docs/en/*/bees.svg
```
![](mermaid-diagram-20210224082643.svg)
* Image at work
  * To square, [https://www.oddprints.com/edit](https://www.oddprints.com/edit)
  * To resize JPG, [https://imagemagick.org/index.php](https://imagemagick.org/index.php)
```bash
convert sunflower.jpg -resize 15% sun15.jpg
```  
* Favicon
  * To generate favicon, [https://realfavicongenerator.net/](https://realfavicongenerator.net/)
* Site logo
  * To generate/resize SVG, [https://inkscape.org/](https://inkscape.org/)
  * To replace logo.svg at assets/image/logo and _includes/svg
* Project icon
  * To crop circle, [https://crop-circle.imageonline.co/](https://crop-circle.imageonline.co/)
  * To generate/resize SVG, [https://inkscape.org/](https://inkscape.org/)
  * To resize SVG (simpler), [https://www.iloveimg.com/resize-image/resize-svg](https://www.iloveimg.com/resize-image/resize-svg)
 
---

```javascript
(() => console.log('Updated!'))();
```
