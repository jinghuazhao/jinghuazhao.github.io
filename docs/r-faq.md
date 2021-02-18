---
layout: article
title: FAQs for the R packages distributed by Jing Hua Zhao
---

Packages **kinship**, **lmm** and **pan** were ported from S-PLUS
packages by Beth Atkinson, Terry Therneau and Joseph L Schafer, while
**tdthap** was based on a version of R package by David Clayton; you can
always send your questions directly to these authors.

-   **Q.** Is there anything wrong with the code in **gap**, that
    *gc.em* and *hap.em* give me codes hap1code and hap2code that do not
    make sense to me?
-   **A.** Apparently no, they are the unique haplotype identifiers,
    mixed-radixed numbers based on alleles at each marker locus.
    However, if you do want to find out how they are formed, there is an
    internal function revhap(loci,id) to unfold the alleles. For
    instance, cat(revhap(c(2,2,3),5)) gives values 1,2,2, for with two
    biallelic and a triallelic loci, the natural sequence of haplotypes
    are 111,112,113,121,122, with1,2,2 being the fifth.

<!-- -->

-   **Q.** When I run *coxme* in **kinship** package, there is an error
    message saying function \"coxph.wtest not found\"; can I fix this?
-   **A.** This is to do with **survival** package, which contains the
    function in R 1.8.1 but not R 1.9.x. Ideally this will be fixed in
    the next version of **survival**. In case this problem remains, you
    can try the following tricks if you use Windows:
    -   Start R 1.8.1, issue command library(survival),
        sink(\"c:/coxph.wtest.R\"), coxph.wtest, sink()
    -   Start R 1.9.x, issue command coxph.wtest \<-
        source(\"c:/coxph.wtest.R\")

<!-- -->

-   **Q.** Are there any examples of using **pan** and ****kinship****?
-   **A.** The examples are distributed with the source packages
    (*inst/tests*), and *tests* directory for the installed packages.
    More references about **pan** are as follows,

    > Schafer JL (2001). Multiple imputation with PAN. In Sayer AG,
    > Collins LM (Eds.), New methods for the analysis of change (pp.
    > 357--377). American Psychological Association, Washington, DC.\
    > Schafer JL, Graham JW (2002). Missing data: our view of the state
    > of the art. Psychological Methods. 7:147-177\
    > Schafer J L, Yucel RM (2002). Computational strategies for
    > multivariate linear mixed-effects models with missing values.
    > Journal of Computational and Graphical Statistics. 11:437-457\
    > Demirtas H (2004). Simulation driven inference for multiply
    > imputed longitudinal datasets. Statistica Neerlandica 58:466-482

-   **Q.** I am using IBD information from SOLAR with **kinship**, but
    *coxme* stops due to nonpositive definite matrices.
-   **A.** There is a message from Terry Therneau attached below.

> Date: Sat, 13 Nov 2004 08:13:58 -0600 (CST)\
> From: Terry Therneau \<therneau@mayo.edu\>\
> To: j.zhao@ucl.ac.uk\
> Subject: Re: kinship
>
> We also ran into the problem of non-positive-definite matrices from
> SOLAR.\
> And it is true\-- the IBD matrices that it produces are not postitive
> definite.\
> We had 2 solutions:
>
> 1\. Realize that coxme will be happy as long as the overall variance
> matrix\
> for the random effects is positive-definite. This can be guarrantteed
> with\
> just a little bit on the diagonal:
>
> \> kmat \<- makekinship( ) however it was created\
> \> smat \<- bdsmatrix.ibd(\.... data from SOLAR\
> \> imat \<- bdsI(dimnames(kmat)\[\[1\]\], kmat\$blocksize) \#identity
> matrix
>
> \> coxme( \...\...., varlist=list(imat, kmat, smat),
> variance=c(.01,0,0) )
>
> This adds .01 to the diagonal of the overall variance matrix, and
> keeps the\
> matrix positive definite.
>
> 2\. Get our IBD matrices from simwalk, which produces correct ones.
>
> Note that the error in SOLAR is small roundoff ones. As long as the\
> variance component of the kinship matrix is moderate, it overcomes
> this.\
> But if the program ever, sometime in searching for the solution, tried
> one\
> that had the variance for kmat approx 0 (less than the size of this
> round\
> off error, about .001), then the Cholesky decomp of the overall
> variance fails\
> and the program dies.
>
> We found that adding a very little bit of diagonal worked, but didn\'t
> ever\
> get around to \"proving\" that it should, or how much you really need.
> In\
> linear models this problem doesn\'t occur, because the error variance
> adds\
> enough to the diagonal.
>
> Terry Therneau

*Date last changed 26/1/2014*
