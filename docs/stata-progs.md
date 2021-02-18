---
layout: article
title: Stata programs by Jing Hua Zhao
---

The following is for Hardy-Weinberg equilibrium exact test.

```stata
program stata_snphwe, plugin using ("stata\_snphwe.plugin")
/*an testing example for Stata*/
input all_aa all_ab all_bb
1 2 3
10 20 30
100 200 300
end
qui gen p=.
forval i=1/`_N' {
         local aa=all_aa[`i']
         local ab=all_ab[`i']
         local bb=all_bb[`i']
        qui genhwi `aa' `ab' `bb'
        qui replace p=r(p_exact) in `i'
}
list
qui gen p_exact=.
plugin call stata_snphwe all_aa all_ab all_bb p_exact
list
```
The C code below is contained in
[stata\_snphwe.c](software/stata_snphwe.c). It works on summary genotype
data and for one genome-wide association analysis it would take 30-node
Linux cluster 40 days with
[genhw](http://biostat-resources.com/stata/des_genhw.htm) but only
within an hour using this code. A SAS counterpart has also been
implemented.

I have also used C to connect MySQL as is shown (in
[connect\_to\_mysql.do](software/connect_to_mysql.do) and
[connect\_to\_mysql.c](software/connect_to_mysql.c))
here.

*Date last changed* 22/10/2012
