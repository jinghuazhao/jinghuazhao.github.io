---
layout: article
title: R packages Maintained by Jing Hua Zhao
---

This section now has a new home, [https://jinghuazhao.github.io/R/](https://jinghuazhao.github.io/R/).

It is still possible to install `kinship` as follows,
```r
install.packages("kinship",contriburl="http://jhz22.user.srcf.net/software")
install.packages("kinship","R",contriburl="http://jhz22.user.srcf.net/software")
```
but it is also possible to install these packages, both archived and active, from GitHub, e.g.,

```r
library(devtools)
install_github("cran/kinship")
```
Here are some frequently-asked questions [FAQs](r-faq.md).

The [associate R program](software/gaw14.R) generates the gaw14.dot files which are converted to .pdf by [graphviz](http://www.graphviz.org)/Gvedit.

**Source**                          | **Raw data**                     | **dot program**                 |  **dot diagram**            |  **fdp diagram**
------------------------------------|----------------------------------|---------------------------------|-----------------------------|----------------------
[GAW14](http://www.gaworkshop.org)  | [gaw14.pre](software/gaw14.pre)  | [gaw14.dot](software/gaw14.dot) |  [dot.pdf](software/dot.pdf)|   [fdp.pdf](software/fdp.pdf)
------------------------------------|----------------------------------|---------------------------------|-----------------------------|-----------------------------

Packages | Comments
-----------------------------------|-----------------------------------
 **Bundle:**                       | [CGR](software/CGR_1.0-5.tar.gz) ([Windows version](software/CGR_1.0-5.zip))
-----------------------------------|-----------------------------------
 **Version:**                      | 1.0-5                             
-----------------------------------|-----------------------------------
 **Date:**                         | 2006-5-22                         
-----------------------------------|-----------------------------------
 **Title:**                        | Classic Genetics in R             
-----------------------------------|-----------------------------------
 **Author:**                       | Jing hua Zhao in collaboration with other colleagues             
-----------------------------------|-----------------------------------
 **BundleDescription:**            | This is an experimental package bundle based on the R packages    
                                   | pathmix and pointer.              
-----------------------------------|-----------------------------------
 **License:**                      | Programs included in this package by Jing hua Zhao will be under    
                                   | GPL. Specific requirement may be possible for programs written by  
                                   | other authors.                    
-----------------------------------|-----------------------------------
 **Name:**                         | [kinship](software/kinship_1.1.4.tar.gz) ([Windows version](software/kinship_1.1.4.zip))
-----------------------------------|-----------------------------------
 **Version:**                      | 1.1.4                             
-----------------------------------|-----------------------------------
 **Date:**                         | 2012-10-15                        
-----------------------------------|-----------------------------------
 **Title:**                        | mixed-effects Cox models, sparse matrices, and modeling data from  
                                   | large pedigrees                   
-----------------------------------|-----------------------------------
 **Author:**                       | Beth Atkinson (<atkinson@mayo.edu>) for pedigree functions.
                                   | Terry Therneau (<therneau@mayo.edu>) for all other functions.          
-----------------------------------|-----------------------------------
 **Depends:**                      | survival, nlme, lattice           
-----------------------------------|-----------------------------------
 **Description:**                  | coxme: general mixed-effects Cox models; kinship: routines to      
                                   | create and manipulate n by n matrices that describe the        
                                   | genetic relationships between n persons; pedigree: create and     
                                   | plot pedigrees; bdsmatrix: a class of objects for sparse       
                                   | block-diagonal matrices (which is how kinship matrices are stored); 
                                   | gchol: generalized cholesky decompositions.
-----------------------------------|-----------------------------------
 **License:**                      | GPL (\>=2)                        
-----------------------------------|-----------------------------------

*Date last changed* 16/3/2016
