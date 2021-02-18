---
layout: article
titles:
  # @start locale config
  en      : &EN       Research
  en-GB   : *EN
  en-US   : *EN
  en-CA   : *EN
  en-AU   : *EN
  zh-Hans : &ZH_HANS  研究
  zh      : *ZH_HANS
  zh-CN   : *ZH_HANS
  zh-SG   : *ZH_HANS
  zh-Hant : &ZH_HANT
  zh-TW   : *ZH_HANT
  zh-HK   : *ZH_HANT
  ko      : &KO
  ko-KR   : *KO
  fr      : &FR
  fr-BE   : *FR
  fr-CA   : *FR
  fr-CH   : *FR
  fr-FR   : *FR
  fr-LU   : *FR
  # @end locale config
mathjax: true
mathjax_autoNumber: false
mermaid: true
key: page-research
---

I promoted reproducible research through presentations at
[useR!2007](http://www.user2007.org/),
[useR!2008](http://www.statistik.uni-dortmund.de/useR-2008/tutorials/),
[useR!2009](http://www.r-project.org/conferences/useR-2009/tutorials/index.html),
[useR!2010](http://www.r-project.org/conferences/useR-2010/tutorials/index.html),
[useR!2011](https://www.r-project.org/conferences/useR-2011/), [GWAS course](https://jinghuazhao.github.io/GWAS-course/), Henry-Stewart and
local talks as with [software collections](r-genetics.md). I collected
bookmarks ([MRC](mrclinks.md) with [comments](mrc/comments.txt),
[UCL](ucllinks.md) and [KCL](kcllinks.md) with
[comments](iop/comments.txt) and a [diagram](focus.gif)\--[a mermaid version](iop/focus.png)), 
```mermaid
graph BT;
e1 --> F1(Genetics);
e2 --> F2(Epidemiology);
e3 --> F3(Mathematical Statistics);
e4 --> F4(Computer Science);
B((Genetic Epidemiology & Biostatistics)) --> F1(Genetics);
B((Genetic Epidemiology & Biostatistics)) --> F2(Epidemiology);
B((Genetic Epidemiology & Biostatistics)) --> F3(Mathematical Statistics);
B((Genetic Epidemiology & Biostatistics)) --> F4(Computer Science);
A(Public Health) --> B((Genetic Epidemiology & Biostatistics));
U --> A(Public Health);
```
I created [DSA](https://jinghuazhao.github.io/DSA), [Numerical Analysis](https://jinghuazhao.github.io/Numerical-Analysis),
[Computational Statistics](https://jinghuazhao.github.io/Computational-Statistics/),
[physalia](https://jinghuazhao.github.io/physalia/), [software notes](https://jinghuazhao.github.io/software-notes/), 
[Omics resources](https://github.com/jinghuazhao/Omics-analysis/wiki/Resources),
as well as developed [software](software.md) (esp. [Haplotype Analysis](https://jinghuazhao.github.io/Haplotype-Analysis/),
[R](https://jinghuazhao.github.io/R/) and more recently
[FM-pipeline](https://jinghuazhao.github.io/FM-pipeline/) and
[PW-pipeline](https://jinghuazhao.github.io/PW-pipeline/)) on
[GitHub](https://github.com/jinghuazhao?tab=repositories) and
[CRAN](http://cran.r-project.org/).

The following is an excerpt from the [EWAS-fusion](https://jinghuazhao.github.io/EWAS-fusion/) pipeline.
```mermaid
graph TB;
SNP["LD reference panel (bed,bim,fam)"] --> |"EWAS reference panel(top1, blup, lasso, enet, bslmm)"| Methylation;
Methylation --> Trait;
SNP --> |"GWAS summary statistics (SNP, A1, A2, Z)"| Trait;
```
and the mathematical expression of the test statistic is
$$ z_{EWAS} = \frac{w^T_{me}z_T}{\sqrt{w^T_{me}Vw_{me}}} $$

At CEU, I am part of the [cambridge-ceu](https://cambridge-ceu.github.io/) GitHub organisation.
