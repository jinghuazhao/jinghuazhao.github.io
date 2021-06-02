---
layout: article
title: Shiny Apps
permalink: /en/shinyapps
key: page-shinyapps
show_title: true
sidebar:
  nav: docs-en
---

See [here](https://jinghuazhao.github.io/Computational-Statistics/LANGUAGES/#shinyapps) for information on how these were set up.

* [shinyapps](https://jinghuazhao.shinyapps.io/shinyapps/) ([shiny examples](https://github.com/rstudio/shiny-examples) `hello` with `ui.R` and `server.R` instead of `app.R`) [![](bees.svg)](https://github.com/jinghuazhao/ShinyApps)
* [shinygap](https://jinghuazhao.shinyapps.io/shinygap/) [![](bees.svg)](https://github.com/jinghuazhao/R) (gap/inst/shinygap)
* [shinySurvival](https://jinghuazhao.shinyapps.io/shinysurvival/) [![](bees.svg)](https://github.com/jinghuazhao/ShinyApps)

Given the uncertainty with the Shiny server availability, it is an optional choice to run these locally within RStudio by the following steps:

1. Download the appropriate repository,
2. Enter the directory containing the Shiny app (i.e., ui.R and server.R); for R/gap this is `inst/shinygap` from the source or `shinygap` in the installed package.
3. Start RStudio (through the rstudio command), and issue `library(shiny);runApp()`

Note it is assumed that the required R packages (shiny, gap, survminer) are installed.
