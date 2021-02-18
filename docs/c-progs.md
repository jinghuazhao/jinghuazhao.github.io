---
layout: article
title: C programs by Jing Hua Zhao
---

2LD, EH+, FASTEH+, GENECOUNTING, HAP can be put in the same directory
with call to the appropriate executables. EH+, FASTEH+ and GENECOUNTING
can also share the same parameter and data file. I have tested them
extensively under Windows, Sun, Dec Alpha and Linux systems. A brief
comparison is shown in the following table. Program MCETDT (Monte Carlo
module for the Extended Transmission Disequilibrium Test) is distributed
with ETDT and unavailable from this site. Note to enter MS-DOS under the
default setup for Windows Visa, you need to run
c:\\windows\\system32\\cmd.exe first.

Package name | Executable names| Documentation | Features | Limitations
-------------|-----------------|---------------|----------|------------
**2LD**| `2ld` | `2ld.doc`, `2ld.htm` |  D', SE(D'), Cramer's V for two multiallelic loci, r | Requires **LDSHELL** for many markers, does not show D' in graphics
**EH+** | `eh`, `ehplus`, `fehp`, `pm`, `pmplus` | `pm.doc`, `pm.stm` |  Model-free and permutation tests of allelic association. **EH** compatible and very easy to use. (having been the top paper in Hum Hered in 2005/6/7). | Slower than **FASTEH+** and **GENECOUNTING** but call **FASTEH+** for permutation tests from version 1.2
**FASTEH+** | `fpmp`,`fehp`,`pfehp` | `fpmp.doc` | Faster algorithm and likelihood-based LD measures | Does not handle missing data, less statistics than **EH+**
**GENECOUNTING**  | `gc`,`gcp`,`gcx`,`pgc` | `gc.txt` | Haplotype frequency estimation and reconstruction, flexible in missing data patterns and X chromosome data, haplotype-specific tests | Limited to about 15 SNPs and slow with multiple multiallelic loci with missing data
**HAP** |  `hap`,`mia` | `hap.txt` | Large number of SNPs and multiple imputations, missing data, multiallelic loci | Possibly sub-optimal solution

-   **2LD**
    -   full name: Two-locus linkage disequilibrium (LD) calculator
    -   description: [online documentation](software/2ld.htm) and a
        brief [Adobe PDF](software/2ld.pdf)/[Word DOC](software/2ld.doc)
        documentation by [Dr David
        Collier](http://www.iop.kcl.ac.uk/staff/profile/?go=10610)
    -   web: [2ld.zip](software/2ld.zip)
    -   source code language: C
    -   systems: PC, Unix (SUN Solaris and Linux)
    -   reference:
        -   [Zhao, J. H. (2004) \"2LD, GENECOUNTING and HAP: Computer
            programs for linkage disequilibrium analysis\".
            Bioinformatics, 20, 1325-1326](paper/bi04.pdf)
        -   [Zapata C, Carollo C, Rodriguez S. (2001) \"Sampling
            variance and distribution of the D\' measure of overall
            gametic disequlibrium between multiallelic loci\". Annals of
            Human Genetics, 65, 395-406.](paper/zapata01.pdf)
-   **EH+** or **EHPLUS**
    -   full name: Model-free analysis and permutation tests for allelic
        association
    -   version: 1.0, 1.1, 1.2
    -   descriptions: [documentation](software/pm.htm)
    -   source code language: C
    -   web: v [1.0](software/pm10.zip), [1.1](software/pm11.zip),
        [1.2](software/pm12.zip), [2.0](software/pm20.zip)
    -   operating systems: PC and Unix (DEC OSF, Sun Solaris,
        [Linux]{style="COLOR: red"})
    -   [reference: ]{lang="PT-BR"}[[Zhao, J. H., Curtis, D., Sham, P.
        C. (2000). ]{lang="PT-BR"}\"Model-free analysis and permutation
        tests for allelic associations\". Human Heredity, 50(2),
        133-139](paper/hh00.pdf).
-   **FASTEH+** or **FASTEHPLUS**
    -   full name: faster EH+
    -   descriptioin: made available in the spirit of Knuth (1998) with
        [documentation](software/fpmp.pdf) (PDF)
    -   web: [fehp.zip](software/fehp.zip)
    -   source code language: C
    -   systems: PC, Unix (DEC OSF, SUN Solaris and Linux)
    -   reference: [Zhao, J. H., Sham, P. C. (2002) \"Faster allelic
        association analysis using unrelated subjects\". Human Heredity,
        53(1), 36-41.](paper/hh02.pdf)
-   **GENECOUNTING**
    -   full name: gene-counting for haplotype analysis with permutation
        tests for global association and specific haplotypes, accounting
        for missing data
    -   [description: executable programs with
        ]{lang="FR"}[[documentation](software/gc.pdf) ]{lang="FR"}
    -   web: v [1.0](software/gc.zip), [1.1](software/gc11.zip),
        [1.2](software/gc12.zip), [1.3](software/gc13.zip),
        [2.0](software/gc20.zip), [2.1](software/gc21.zip),
        [2.2](software/gc22.zip)
    -   source code language: C. A version with source code (for
        autosomal data) and utility programs can be found in
        [here](http://www.mds.qmul.ac.uk/statgen/dcurtis/software.html).
    -   systems: PC, Unix (SUN Solaris and Linux)
    -   reference:
        -   [Zhao, J. H, .Lissarrague, S., Essioux, L., Sham, P.
            C. (2002) \"GENECOUNTING: haplotype analysis with missing
            genotypes\" Bioinformatics, 18(12),
            1694-1695](paper/bi02.pdf).
        -   [Zhao, J. H. (2004) \"2LD, GENECOUNTING and HAP: Computer
            programs for linkage disequilibrium analysis\".
            Bioinformatics, 20, 1325-1326](paper/bi04.pdf)
-   **HAP**
    -   full name: haplotype analysis of polymorphic markers
    -   descriptioin: extension of
        [SNPHAP](http://www-gene.cimr.cam.ac.uk/clayton/software/snphap.txt)
    -   web: v [0.2.1](software/hap.zip)
    -   source code language: C
    -   systems: PC, Unix (SUN Solaris and Linux)
    -   reference:[Zhao, J. H. (2004) \"2LD, GENECOUNTING and HAP:
        Computer programs for linkage disequilibrium analysis\".
        Bioinformatics, 20, 1325-1326](paper/bi04.pdf)
