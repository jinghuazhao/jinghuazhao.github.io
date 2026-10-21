# 29-11-2013 MRC-Epid JHZ

gaw14 <- read.table("gaw14.pre", as.is=TRUE, header=FALSE)
names(gaw14) <- c("pid","id", "fid", "mid", "sex", "aff")

library(gap)
pedtodot(gaw14, page="A4", height=0.25, width=0.25, rotate=90, dir="forward")

