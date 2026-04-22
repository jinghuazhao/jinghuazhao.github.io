---
layout: article
title: A full stack Locuszoom.js application (updated)
tags: [info, Genetics]
mathjax: true
mathjax_autoNumber: false
mermaid: true
---

## Update (10/1/2025)

This is fully updated at <https://jinghuazhao.github.io/pQTLtools/articles/LocusZoom.js.html>.

## Original post

This is built on A1BG & ACE, <https://jinghuazhao.github.io/Caprion/lz.htm>

```bash
# (nearest) code for caprion_dr.js
# toJSON(list(ppid=paste0(prot,"-",pqtl),data=d,analysis=paste0(prot,"-",pqtl)),auto_unbox=TRUE,pretty=FALSE)
export suffix=_dr
Rscript -e '
    library(dplyr)
    library(jsonlite)
    suffix <- Sys.getenv("suffix")
    vars <- c("variant","position","ref_allele","alt_allele_freq","beta","log_pvalue")
    merged_data <- list()
    jsonlist <- dir(pattern="json")
    flist <- grep("A1BG|ACE",jsonlist,value=TRUE)
    for (i in 1:length(flist))
    {
      s <- unlist(strsplit(flist[i],"-|[.]"))
      f <- list(ppid=paste0(s[1],"-",s[2]),data=fromJSON(flist[i])$data[vars])
      merged_data <- c(merged_data,list(f))
    }
    merged_json <- toJSON(merged_data)
    sink(paste0("caprion",suffix,".js"))
    cat("input=")
    writeLines(merged_json)
    sink()
    decouple <- function(f)
    {
      d <- fromJSON(f)
      for (i in 1:nrow(d))
      {
        di <- with(d,list(ppid=ppid[[i]],data=data[[i]]))
        sink(paste0(i-1,".json"))
        writeLines(toJSON(di))
        sink()
      }
    }
'
```

<!--more-->
