---
layout: article
title: pQTLtools 0.4 is checked!
tags: pQTLtools
mathjax: true
mathjax_autoNumber: false
mermaid: true
---

We see output from

```bash
R CMD check --as-cran pQTLtools_0.4.tar.gz
```
as in `inst/csd3.sh`:

```
Loading ceuadmin/R/latest
  Loading requirement: curl/7.79.0/gcc/75dxv7ac libiconv/1.16/gcc/aa2kwjch libxml2/2.9.13/gcc/fww2yzpt ncurses/6.2/gcc/qke6jyyt
    gettext/0.21/gcc/lhdl4tbr pcre2/10.39/gcc/inuagvoq readline/8.1/gcc/bgw44yb2 hdf5/1.12.1 icu4c/67.1/gcc/maavowaj
    jags-4.3.0-gcc-5.4.0-4z5shby mono/5.0.1.1 libmatheval/intel/1.1.11 hdf5/impi/1.8.16 netcdf/4.4.1 ceuadmin/json-c/0.17-20230812-icelake
    ceuadmin/libsodium/1.0.20 ceuadmin/libpng/1.5.30 ceuadmin/libssh/0.10.6-icelake ceuadmin/openssh/9.7p1-icelake ceuadmin/qpdf/11.9.1
    ceuadmin/nettle/2.7.1 texlive/2015 ceuadmin/gsl/2.7.1 libpng/1.6.37/gcc/bkdpz5q4 libiconv/1.16/gcc/4miyzf3w libxml2/2.9.12/gcc/eizlvpgn
    ceuadmin/readline/8.0 ceuadmin/ImageMagick/7.1.1-31 ceuadmin/libgit2/1.4.2 lz4-1.7.5-gcc-5.4.0-qkdvk4q python/3.7 ceuadmin/NLopt/2.7.1
    ceuadmin/openssl/3.2.1-icelake ceuadmin/poppler/0.84.0 ceuadmin/glpk/4.57 ceuadmin/icu/70.1 ceuadmin/krb5/1.21.2-icelake
    ceuadmin/rust/1.74.1
* checking for file ‘pQTLtools/DESCRIPTION’ ... OK
* preparing ‘pQTLtools’:
* checking DESCRIPTION meta-information ... OK
* installing the package to process help pages
Loading required namespace: pQTLtools
* saving partial Rd database
* creating vignettes ...
 OK
* checking for LF line-endings in source and make files and shell scripts
* checking for empty or unneeded directories
Removed empty directory ‘pQTLtools/inst/snakemake/output/MR’
Removed empty directory ‘pQTLtools/inst/snakemake/output’
* re-saving image files
* building ‘pQTLtools_0.4.tar.gz’

* installing to library ‘/rds/project/rds-4o5vpvAowP0/software/R’
* installing *source* package ‘pQTLtools’ ...
** using staged installation
** R
** data
*** moving datasets to lazyload DB
** inst
** byte-compile and prepare package for lazy loading
Note: more than one default provided in switch() call
** help
*** installing help indices
*** copying figures
** building package indices
** installing vignettes
** testing if installed package can be loaded from temporary location
** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (pQTLtools)
* using log directory ‘/home/jhz22/pQTLtools.Rcheck’
* using R version 4.4.2 (2024-10-31)
* using platform: x86_64-pc-linux-gnu
* R was compiled by
    gcc (GCC) 8.5.0 20210514 (Red Hat 8.5.0-22)
    GNU Fortran (GCC) 8.5.0 20210514 (Red Hat 8.5.0-22)
* running under: Rocky Linux 8.10 (Green Obsidian)
* using session charset: UTF-8
* using option ‘--as-cran’
* checking for file ‘pQTLtools/DESCRIPTION’ ... OK
* checking extension type ... Package
* this is package ‘pQTLtools’ version ‘0.4’
* package encoding: UTF-8
* checking CRAN incoming feasibility ... [4s/142s] WARNING
Maintainer: ‘Jing Hua Zhao <jinghuazhao@hotmail.com>’

New submission

Unknown, possibly misspelled, fields in DESCRIPTION:
  ‘Remotes’

Strong dependencies not in mainstream repositories:
  pQTLdata
Suggests or Enhances not in mainstream repositories:
  gwasvcf, TwoSampleMR, phenoscanner

Found the following (possibly) invalid URLs:
  URL: http://www.phenoscanner.medschl.cam.ac.uk/
    From: DESCRIPTION
          man/pQTLtools.Rd
    Status: Error
    Message: libcurl error code 28:
        Connection timed out after 60001 milliseconds
  URL: https://jinghuazhao.github.io/pQTLtools (moved to https://jinghuazhao.github.io/pQTLtools/)
    From: DESCRIPTION
          man/pQTLtools.Rd
    Status: 200
    Message: OK
* checking package namespace information ... OK
* checking package dependencies ... OK
* checking if this is a source package ... OK
* checking if there is a namespace ... OK
* checking for executable files ... OK
* checking for hidden files and directories ... OK
* checking for portable file names ... OK
* checking for sufficient/correct file permissions ... OK
* checking whether package ‘pQTLtools’ can be installed ... [14s/19s] OK
* checking installed package size ... NOTE
  installed size is  9.5Mb
  sub-directories of 1Mb or more:
    doc         1.3Mb
    help        1.3Mb
    snakemake   1.9Mb
    turboman    1.9Mb
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
* checking loading without being on the library search path ... OK
* checking use of S3 registration ... OK
* checking dependencies in R code ... OK
* checking S3 generic/method consistency ... OK
* checking replacement functions ... OK
* checking foreign function calls ... OK
* checking R code for possible problems ... [19s/20s] OK
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
* checking examples ... [23s/30s] NOTE
Examples with CPU (user + system) or elapsed time > 5s
                 user system elapsed
run_TwoSampleMR 8.229  0.251  12.485
* checking for unstated dependencies in vignettes ... OK
* checking package vignettes ... OK
* checking re-building of vignette outputs ... [251s/489s] OK
* checking PDF version of manual ... OK
* checking HTML version of manual ... OK
* checking for non-standard things in the check directory ... OK
* checking for detritus in the temp directory ... OK
* DONE

Status: 1 WARNING, 2 NOTEs
See
  ‘/home/jhz22/pQTLtools.Rcheck/00check.log’
for details.
```
