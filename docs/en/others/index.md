---
layout: article
key: page-others
footer: true
show_title: false
sidebar:
  nav: docs-en
show_title: false
---

# Other projects

* Epigenomics
  * [EWAS-fusion](https://jinghuazhao.github.io/EWAS-fusion/)[^longnote] ([GitHub](https://github.com/jinghuazhao/EWAS-fusion))
  * [QTR](https://jinghuazhao.github.io/QTR/) ([GitHub](https://github.com/jinghuazhao/QTR))

* Genomics
  * [FM-pipeline](https://jinghuazhao.github.io/FM-pipeline/) ([GitHub](https://github.com/jinghuazhao/FM-pipeline))
  * [hess-pipeline](https://jinghuazhao.github.io/hess-pipeline/) ([GitHub](https://github.com/jinghuazhao/hess-pipeline))
  * [PW-pipeline](https://jinghuazhao.github.io/PW-pipeline/) ([GitHub](https://github.com/jinghuazhao/PW-pipeline))
  * [SUMSTATS](https://jinghuazhao.github.io/SUMSTATS/) ([GitHub](https://github.com/jinghuazhao/SUMSTATS))
  * [TWAS-pipeline](https://jinghuazhao.github.io/TWAS-pipeline/) ([GitHub](https://github.com/jinghuazhao/TWAS-pipeline))

* Proteomics
  * [Caprion](https://jinghuazhao.github.io/Caprion/) ([GitHub](https://github.com/jinghuazhao/Caprion))
  * [Olink-NGS](https://jinghuazhao.github.io/Olink-NGS/) ([GitHub](https://github.com/jinghuazhao/Olink-NGS))
  * [SomaLogic](https://jinghuazhao.github.io/SomaLogic/) ([GitHub](https://github.com/jinghuazhao/SomaLogic))
  * [SWATH-MS](https://jinghuazhao.github.io/SWATH-MS/) ([GitHub](https://github.com/jinghuazhao/SWATH-MS))

* Statistics
  * [Computational statistics](https://jinghuazhao.github.io/Computational-Statistics/) ([GitHub](https://github.com/jinghuazhao/Computational-Statistics))
  * [DSA](https://jinghuazhao.github.io/DSA/) ([GitHub](https://github.com/jinghuazhao/DSA))
  * [Mixed models](https://jinghuazhao.github.io/Mixed-Models/) ([GitHub](https://github.com/jinghuazhao/Mixed-Models))
  * [Numerical analysis](https://jinghuazhao.github.io/Numerical-Analysis/) ([GitHub](https://github.com/jinghuazhao/Numerical-Analysis))

* Miscellaneous categories
  * [GDCT](https://jinghuazhao.github.io/GDCT/) ([GitHub](https://github.com/jinghuazhao/GDCT))
  * [GWAS course](https://jinghuazhao.github.io/GWAS-course/) ([GitHub](https://github.com/jinghuazhao/GWAS-course))
  * [Omics-analysis](https://jinghuazhao.github.io/Omics-analysis/) ([GitHub](https://github.com/jinghuazhao/Omics-analysis))
  * [PhD](https://jinghuazhao.github.io/PhD/) ([GitHub](https://github.com/jinghuazhao/PhD))
  * [physalia](https://jinghuazhao.github.io/physalia/) ([GitHub](https://github.com/jinghuazhao/physalia))
  * [Software notes](https://jinghuazhao.github.io/software-notes/) ([GitHub](https://github.com/jinghuazhao/software-notes))

[^longnote]: Transcriptomewide association statistic $z_{TWAS}$ was originally proposed for gene expression data. For a given Trait of interest **T** for which GWAS summary statistics $z_T$ is available, the corresponding Wald statistic for TWAS is defined such that $$z_{TWAS} = \frac{w^T_{ge}z_T}{\sqrt{w^T_{ge}Vw_{ge}}}$$ where $w_{ge}$ is a weight associated with gene expression and **V** covariance matrix for $z_T$, respectively. By analogy, an epigenomewide association statistic $z_{EWAS}$ is defined through methylation data so that $$z_{EWAS} = \frac{w^T_{me}z_T}{\sqrt{w^T_{me}Vw_{me}}}$$ where $w_{me}$ is the weight associated with methylation. Both approaches allow for imputation using GWAS summary statistics. The derivation of these weights and imputation were done using methods called Functional Summary-based Imputation (FUSION).
