---
layout: article
title: Hello, world!
tags: info
mermaid: true
---

# The jekyll-themed site is up!

<!--more-->

# NOTES

* Old page: [https://jhz22.user.srcf.net/](https://jhz22.user.srcf.net/)

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
* favicon
  * To generate favicon, [https://realfavicongenerator.net/](https://realfavicongenerator.net/)
* logos for site and projects
  * To generate SVG, [https://inkscape.org/](https://inkscape.org/)
  * To replace logo.svg at assets/image/logo and _includes/svg
  * To resize SVG, [https://www.iloveimg.com/resize-image/resize-svg](https://www.iloveimg.com/resize-image/resize-svg)
* Icons at projects
  * To crop circle: [https://crop-circle.imageonline.co/](https://crop-circle.imageonline.co/)
 
---

```javascript
(() => console.log('Updated!'))();
```
