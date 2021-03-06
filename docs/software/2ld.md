### 2LD -- two-locus LD calculator

JH Zhao 15/02/2002

[Program description](#anchor274372)  
[Running 2ld](#anchor275325)  
[File listing](#anchor276027)  
[Known problems](#anchor276439)  
[Acknowledgements](#anchor276861)  
[Contact information](#anchor282417)  
[References](#anchor277263)  

#### Program description

2LD is a simple program calculating linkage disequilibrium (LD) measures between two polymorphic markers. It is developed as a supplement for an Excel calculator by Dr David Collier, adding standard errors and handling multiallelic markers.

Denote the number of alleles at markers 1 and 2 as m and n, the observed data can be organized into a contingency table of m(m+1)/2 x n(n+1)/2 cells. However table can be parameterised by only m x n possible haplotype frequencies. As illustrated by ASSOCIATE, an ordinary chi-squared statistic will have [m(m+1)/2-1][n(n+1)/2-1] degrees of freedom and this test of independence may imply dependence other than allelic association. The haplotypes at linkage equilibrium can be obtained from allele frequencies of each marker, while assuming LD they are estimated using a gene-counting procedure. Alternatively, haplotype frequency estimates from other sources can also be used. In addition, the program gives chi-squared test of the estimated haplotype frequencies, as a global measure of LD, i.e. Phi coefficient and Cramer's V. However this will need asymptotic approximation, Fisher's exact test may be more appropriate for its significance. Finally 2ld calculates another popular measure of LD, D' and standard error. As yet 2ld does not handle missing genotypes.

Computer programs ASSOCIATE and EH also implement gene-counting procedure, and are available from http://linkage.rockefeller.edu.

For more details see Klitz et al. (1995), Long et al. (1995), Weir (1996) and other references listed below. To obtain permutation-based LD measures use PM or FASTEH+ at this site.

#### Running 2ld

2ld will accept an input file in one of the three formats.

**Format 1**. the raw genotype data in consecutive lines, each line containing five columns as follows.

Column 1\. Individual ID  
Column 2, 3\. Marker 1 genotypes  
Column 4, 5\. Marker 2 genotypes

File genotype.dat is in this format.

**Format 2**. genotype table as required by ASSOCIATE and EH programs

Line 1\. < No of alleles at marker 1> <No of alleles at marker 2>  
Line 2- actual two-locus genotype counts

File genotype.tab is in this format. Note that since the two markers have alleles 14 and 2, the genotype table has 14(14+1)/2 x 2(2+1)/2 = 105 x 3 cells.

**Format 3**. observed haplotype frequencies from any other sources.

Line 1.  
<# of alleles at marker 1> <# of alleles at marker 2> <# of subjects>  
Line 2-  
haplotype frequencies

File genotype.eh, 2by2.dat, kbyl.dat are in this format. Note if haplotype frequency estimates are based on EH then the column "w/association" in the output has to be used. Since 2ld was designed for diploid individuals, the number of haplotypes is equal to twice the number of subjects.

The syntax of 2ld is as follows,

2ld <data file>

We use convention of DOS that ``data file'' within angled bracket is needed; otherwise the program only gives the internal example. The screen output can be redirected to a ASCII file by using "> output file name". For a case-control study three separate input files can be created, for cases only, controls only and combined. To run 2ld on 2by2.dat the command is

2ld 2by2.dat

to output on computer screen,

or

2ld 2by2.dat >2by2.out

to output to file 2by2.out

#### File listing

<menu>*   <font face="Courier New">2ld.c    C source</font>*   <font face="Courier New">2ld.exe  Win9x executable</font>*   <font face="Courier New">2ld.txt  this file</font>*   <font face="Courier New">2by2.dat sample data file for two biallelic markers</font>*   <font face="Courier New">kbyl.dat sample data file for two multiallelic markers</font>*   <font face="Courier New">genotype.dat an example of directly using raw genotype data</font>*   <font face="Courier New">genotype.tab an example of directly using EH input file</font>*   <font face="Courier New">genotype.eh EH output file on genotype.dat, genotype.tab</font></menu>

2ld.c is in ANSI C so should be portable to Unix/Linux. 2ld.exe is created from 2ld.c by Symantec C/C++ 7.2 compiler with command "sc -mn 2ld.c".

#### Known problems

> Q

2ld.exe always gives internal example if clicking 2ld.exe from Win9x, when I press <Return>, even 2ld window disappears.

> A

Since 2ld is a DOS-based program, Windows users will have to enter MS-DOS Prompt first. For example under Win9x, click Start -> Program -> MS-DOS Prompt, change to the appropriate directory and issue 2ld command described above. I put 2ld.exe in c:\iop\2ld directory, so my commands would be

cd c:\iop\2ld  
2ld 2by2.dat >2by2.out  
edit 2by2.out

Alternatively I can add 2ld directory by DOS command

set path=c:\iop\2ld;%path%

then I can use 2ld anywhere under DOS.

> Q

Why my degree(s) of freedom differ from EH ?

> A

2LD calculates degree(s) of freedom from alleles present, rather than user-specified.

> Q

I get two D's, one negative and one positive, for my biallelic data, why?

> A> Q

I get two D's, one negative and one positive, for two biallelic data, why?

> A

When there are 2 biallelic markers involved, let p_1, p_2 be allele frequencies  
at locus 1, and q_1, q_2 be allele frequencies at locus 2\. The first D' is  
given under "Disequilibria, expectations and variances" as D'_{11}, i.e., D'  
for haplotype 11, while the second D' is obtained as follows,

p_1q_1|D'_{11}|+p_1q_2|D'_{12}|+p_2q_1|D'_{21}|+p_2q_2|D'_{22}|

They happen to have the same quantity but may differ in signs.  

> Q

How to get more sense of the global chi-square ?

> A

A chi-square based on the estimated haplotype frequency table, as a direct test of global disequilibrium. A simple check can be done with standard packages such as SAS. For example the following program computes chi-square and Fisher's exact test for a biallelic marker and a three-allele marker from 21 diploid individuals (data kindly from Dr Zhicheng Lin).

data abc;  
input a b w;  
w=round(w*42);  
cards;  
1 1 0.095234  
1 2 0.000005  
1 3 0.047618  
2 1 0.238099  
2 2 0.571423  
2 3 0.047621  
;  
proc freq;  
weight w;  
table a*b/chisq exact;  
run;

Unfortunately there is no degree of freedom for a test between this and that from EH, for both chi-squares have (m-1)(n-1) degrees of freedom.

> Q

I have 5 loci in my data set, and 6 populations. Is it possible to use 1 working file and include parameters for which pop and locus pair to analysis?

> A (this is now part of LDSHELL)

I imagined it was much of a work to have everything in one go and didn't implement it. Now I spent >1 days to integrate my program fragments and attach it to you. As usual you will need unzip it first. I wrote it in a haste so please let me know if there is any problem with it.

Basically you can organize your subjects as follows,

id popid m11 m12 m21 m22 m31 m32 m41 m42 m51 m52

where id is any subject id, popid is a population a subject belongs to, and m's are the marker genotypes/alleles.

Now put ldshell.exe in the same directory as 2LD and type

ldshell yourfilename 5

then check pop##.out for results of each population (## is the population label).

Included also are a file called hla.dat which is in the format aforementioned. Since it has control and case information labelled as 0 and 1, the output files are pop0.out and pop1.out, which are generated using command

ldshell hla.dat 3

To see D' coefficient grep.exe is useful (Under Unix/Linux both unzip and grep are internal):

grep "coefficient =" pop?.out  
POP0.OUT: D' coefficient = 0.970663, SD = 0.0090 (Var = 0.000081)  
POP1.OUT: D' coefficient = 0.824925, SD = 0.0265 (Var = 0.000701)

It should be a good idea to do some random checks to make sure.  

Acknowledgements

A list of people who help to make the program/documentation more useful.

David Collier <sphadco@iop.kcl.ac.uk>  
Zhicheng Lin <ZLIN@intra.nida.nih.gov>  
Mustafa Neamatallah <m_neamatallah@hotmail.com>  
Carlos Zapata <bfcazaba@usc.es>  
Barry Chioza <spbcaja@iop.kcl.ac.uk>  
Maria Arranz <m.arranz@iop.kcl.ac.uk>  
Tan Hui Hui Jenny <medp9193@nus.edu.sg>

#### Contact information

Please let me know your problem or comments by e-mailing j.zhao@iop.kcl.ac.uk or by post to

Jing Hua Zhao

Section of Genetic Epidemiology & Biostatistics  
Division of Psychological Medicine  
Institute of Psychiatry  
De Crespigny Park  
London SE5 8AF  
UK

#### References

Abramowitz M and Stegun IA (1968) Handbook of mathematical functions. New York

Bishop YMM, Fienberg SE, Holland PW (1975) Discrete Multivariate Analysis -- Theory and Practice, The MIT press

Cramer H (1946) Mathematical Methods of Statistics. Princeton Univ. Press

Klitz W, Stephen JC, Grote M, Carrington M (1995) Discordant patterns of linkage disequilibrium of the peptide transporter loci within the HLA class II region. Am. J. Hum. Genet. 57:1436-1444

Long JC, Williams RC, Unbanek M (1995) An E-M algorithm and testing strategy for multiple-locus haplotypes. Am. J. Hum. Genet. 56:799-810

Weir BS (1979) Inferences about linkage disequilibrium. Biometrics 35:235-254

Weir BS (1996) Genetic Data Analysis II. Sinaur

Xie X, Ott J (1993) Testing linkage disequilibrium between a disease gene and marker loci. Am J Hum Genet 53:1107

Zapata C, Alvarez G, Carollo C (1997) Approximate variance of the standardized measure of gametic disequilibrium D'. Am. J. Hum. Genet. 61:771-774

Zapata C, Carollo C, Rodriguez S (2001) Sampling variance and distribution of the D' measure of overall gametic disequlibrium between multiallelic loci. Ann Hum Genet 65:395-406

<center>Last modified: 22/5/2004 by: [Jing Hua Zhao](mailto:jzhao@hgmp.mrc.ac.uk)</center>
