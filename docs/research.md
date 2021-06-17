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
  zh-Hant : &ZH_HANT  研究
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

I have promoted reproducible research through presentations, software implementation and various projects.

## Presentations

* [useR!2007](http://www.user2007.org/),
* [useR!2008](http://www.statistik.uni-dortmund.de/useR-2008/tutorials/),
* [useR!2009](http://www.r-project.org/conferences/useR-2009/tutorials/index.html),
* [useR!2010](http://www.r-project.org/conferences/useR-2010/tutorials/index.html),
* [useR!2011](https://www.r-project.org/conferences/useR-2011/),
* [GWAS course](https://jinghuazhao.github.io/GWAS-course/), 
* Henry-Stewart and local talks

## Bookmarks

* [PHPC](phpclinks.md),
* [MRC](mrclinks.md) with [comments](mrc/comments.txt),
* [UCL](ucllinks.md),
* [KCL](kcllinks.md) with [comments](iop/comments.txt) and a [diagram](focus.gif)\--[a mermaid version](iop/focus.png)), 
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
and [graphviz](grViz.gv) which can be viewed from RStudio.
* [software collections](r-genetics.md).

## Projects

* [consortium](https://jinghuazhao.github.io/en/consortium) projects.
* [other](https://jinghuazhao.github.io/en/others) projects.

## Related activities

At CEU, I am part of the [cambridge-ceu](https://cambridge-ceu.github.io/) GitHub organisation.

## A gentle call

I would appreciate if you [e-mail me](mailto:jinghuazhao@hotmail.com) your comments or information on [citations](references.txt) (Google Scholar on [R/gap](https://tinyurl.com/yxh3ycwg)).
