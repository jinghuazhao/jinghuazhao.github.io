*GET
*  FILE='C:\iop\lecture\class1.sav'.
*EXECUTE .

* ANOVA for MZ.
ANOVA
  VARIABLES=n
  BY id(1 522)
  /MAXORDERS ALL
  /METHOD UNIQUE
  /FORMAT LABELS .

* ANOVA for DZ.
ANOVA
  VARIABLES=n
  BY id(523 794)
  /MAXORDERS ALL
  /METHOD UNIQUE
  /FORMAT LABELS .

COMPUTE wgt =  0.5 .
EXECUTE .

WEIGHT
  BY wgt .

* Intraclass correlation for MZ.
USE ALL.
COMPUTE filter_$=(zyg = 1.0).
VARIABLE LABEL filter_$ 'zyg = 1.0 (FILTER)'.
VALUE LABELS filter_$  0 'Not Selected' 1 'Selected'.
FORMAT filter_$ (f1.0).
FILTER BY filter_$.
EXECUTE .

REGRESSION
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS R ANOVA
  /CRITERIA=PIN(.05) POUT(.10)
  /NOORIGIN
  /DEPENDENT ncotwin
  /METHOD=ENTER n  .

* Intraclass correlation for DZ.
USE ALL.
COMPUTE filter_$=(zyg = 0.5).
VARIABLE LABEL filter_$ 'zyg = 0.5 (FILTER)'.
VALUE LABELS filter_$  0 'Not Selected' 1 'Selected'.
FORMAT filter_$ (f1.0).
FILTER BY filter_$.
EXECUTE .

REGRESSION
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS R ANOVA
  /CRITERIA=PIN(.05) POUT(.10)
  /NOORIGIN
  /DEPENDENT ncotwin
  /METHOD=ENTER n  .

FILTER OFF.
USE ALL.
EXECUTE.

* The overall mean.
DESCRIPTIVES
  VARIABLES=n
  /FORMAT=LABELS NOINDEX
  /STATISTICS=MEAN STDDEV MIN MAX
  /SORT=MEAN (A) .

COMPUTE y = ncotwin - 10.23.
IF (zyg = 1) a = n - 10.23.
IF (zyg = 1) d = n - 10.23.
IF (zyg = 1) c = n - 10.23.

IF (zyg = 0.5) a = (n - 10.23)/2.
IF (zyg = 0.5) d = (n - 10.23)/4.
IF (zyg = 0.5) c = (n - 10.23).
EXECUTE .

* DeFries-Fulker regression.
WEIGHT BY wgt.

REGRESSION
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS R ANOVA
  /CRITERIA=PIN(.05) POUT(.10)
  /ORIGIN
  /DEPENDENT y
  /METHOD=BACKWARD a c.

REGRESSION
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS R ANOVA
  /CRITERIA=PIN(.05) POUT(.10)
  /ORIGIN
  /DEPENDENT y
  /METHOD=ENTER a d.

USE ALL.
COMPUTE filter_$=(n>15).
VARIABLE LABEL filter_$ 'n>15 (FILTER)'.
VALUE LABELS filter_$  0 'Not Selected' 1 'Selected'.
FORMAT filter_$ (f1.0).
FILTER BY filter_$.
EXECUTE .

COMPUTE wgt = 0.845.
WEIGHT BY wgt.

REGRESSION
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS R ANOVA
  /CRITERIA=PIN(.05) POUT(.10)
  /ORIGIN
  /DEPENDENT y
  /METHOD=BACKWARD a c.

REGRESSION
  /MISSING LISTWISE
  /STATISTICS COEFF OUTS R ANOVA
  /CRITERIA=PIN(.05) POUT(.10)
  /ORIGIN
  /DEPENDENT y
  /METHOD=ENTER a d.

FILTER OFF.
USE ALL.
EXECUTE.
