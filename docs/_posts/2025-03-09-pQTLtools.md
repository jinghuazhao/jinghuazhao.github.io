---
layout: article
title: pQTLtools 0.5 starts to take shape
tags: pQTLtools
mathjax: true
mathjax_autoNumber: false
mermaid: true
---

While the vignette remains unchanged, articles are finally reduced to three, featuring Bioconductor, LocusZoom.js, and snakemake, respectively.

At the same time, individualized articles can be recovered from GitHub package release.

See <https://jinghuazhao.github.io/pQTLtools/index.html>.

`R CMD check --as-cran pQTLtools_0.5.tar.gz` generated `00check.log` from Fedora 41 on 25/3/2025,

```
* using log directory ‘/home/jhz22/Downloads/pQTLtools.Rcheck’
* using R Under development (unstable) (2025-02-22 r87796)
* using platform: x86_64-pc-linux-gnu
* R was compiled by
    gcc (GCC) 14.2.1 20250110 (Red Hat 14.2.1-7)
    GNU Fortran (GCC) 14.2.1 20250110 (Red Hat 14.2.1-7)
* running under: Fedora Linux 41 (Workstation Edition)
* using session charset: UTF-8
* using option ‘--as-cran’
* checking for file ‘pQTLtools/DESCRIPTION’ ... OK
* checking extension type ... Package
* this is package ‘pQTLtools’ version ‘0.5’
* package encoding: UTF-8
* checking CRAN incoming feasibility ... [23s/53s] NOTE
Maintainer: ‘Jing Hua Zhao <jinghuazhao@hotmail.com>’

New submission

Unknown, possibly misspelled, fields in DESCRIPTION:
  ‘Remotes’

Suggests or Enhances not in mainstream repositories:
  gwasvcf, TwoSampleMR, phenoscanner

Uses the non-portable packages: ‘MSnbase’, ‘mzR’
* checking package namespace information ... OK
* checking package dependencies ... OK
* checking if this is a source package ... OK
* checking if there is a namespace ... OK
* checking for executable files ... OK
* checking for hidden files and directories ... OK
* checking for portable file names ... OK
* checking for sufficient/correct file permissions ... OK
* checking whether package ‘pQTLtools’ can be installed ... [53s/54s] OK
* checking installed package size ... OK
* checking package directory ... OK
* checking for future file timestamps ... OK
* checking ‘build’ directory ... OK
* checking DESCRIPTION meta-information ... OK
* checking top-level files ... OK
* checking for left-over files ... OK
* checking index information ... OK
* checking package subdirectories ... OK
* checking code files for non-ASCII characters ... OK
* checking R files for syntax errors ... OK
* checking whether the package can be loaded ... OK
* checking whether the package can be loaded with stated dependencies ... OK
* checking whether the package can be unloaded cleanly ... OK
* checking whether the namespace can be loaded with stated dependencies ... OK
* checking whether the namespace can be unloaded cleanly ... OK
* checking use of S3 registration ... OK
* checking dependencies in R code ... OK
* checking S3 generic/method consistency ... OK
* checking replacement functions ... OK
* checking foreign function calls ... OK
* checking R code for possible problems ... [33s/35s] OK
* checking Rd files ... OK
* checking Rd metadata ... OK
* checking Rd line widths ... OK
* checking Rd cross-references ... OK
* checking for missing documentation entries ... OK
* checking for code/documentation mismatches ... OK
* checking Rd \usage sections ... OK
* checking Rd contents ... OK
* checking for unstated dependencies in examples ... OK
* checking contents of ‘data’ directory ... OK
* checking data for non-ASCII characters ... OK
* checking LazyData ... OK
* checking data for ASCII and uncompressed saves ... OK
* checking installed files from ‘inst/doc’ ... OK
* checking files in ‘vignettes’ ... OK
* checking examples ... [38s/41s] NOTE
Examples with CPU (user + system) or elapsed time > 5s
                 user system elapsed
run_TwoSampleMR 4.044 15.725  21.775
* checking for unstated dependencies in vignettes ... OK
* checking package vignettes ... OK
* checking re-building of vignette outputs ... [5m/10m] OK
* checking PDF version of manual ... OK
* checking HTML version of manual ... OK
* checking for non-standard things in the check directory ... OK
* checking for detritus in the temp directory ... OK
* DONE
Status: 2 NOTEs
```
