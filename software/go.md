This document describes a set of SAS program for performing genomewide association analysis. The data are from a study of obesity using population-based case-cohort design. The merits of cohort design in genetic association studies have recently been recognised (Langhholz B. Rothman N., Wacholder S, Thomas DC<font face="Arial"><span style="FONT-SIZE: 12pt; FONT-FAMILY: 'Times New Roman'; mso-fareast-font-family: SimSun; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA">. <span style="FONT-SIZE: 12pt; FONT-FAMILY: 'Times New Roman'; mso-fareast-font-family: SimSun; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA">_J Natl Cancer Inst Monogr 39-42, 1999; Manolio TA, Bailey-Wilson JE, Collins FS_</span><span style="FONT-SIZE: 12pt; FONT-FAMILY: 'Times New Roman'; mso-fareast-font-family: SimSun; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA">. <span style="FONT-SIZE: 12pt; FONT-FAMILY: 'Times New Roman'; mso-fareast-font-family: SimSun; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA"><span style="FONT-SIZE: 12pt; FONT-FAMILY: 'Times New Roman'; mso-fareast-font-family: SimSun; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA">_Nat Rev Genet 7:812-820, 2006_</span></span></span></span>).</font>

The implementation is based on SAS ([http://www.sas.com](http://www.sas.com)), a well-established system for data management, graphics, statistical computing, among others. The rationale for choosing such a system has been documented earlier (Zhao JH, Tan, Q. _Current Bioinformatics_ 1:359-369,2006). The implementation can easily be modified for family-based designs with additional SAS programming or SAS/GENETICS.

There are a number of advantages in this implementation compared to other programs.

*   We do not require any other database management systems (DBMS) or software for graphical presentation. In additional to DATA steps, SAS offers fully functional data access facility through PROC SQL.

*   SAS has a wide variety of procedures for statistical analysis, which will be essential for analysis specific for genomewide association but also for other types of analysis including covariate adjustment, meta-analysis, and so on.

*   All intermediate results will be stored into databases through the output devlirey system (ODS) to be ready for ruther analysis.

*   The users can enjoy the great simplicity in coding which is essential for validity checks. Over years the SAS language is relatively stable and would be ideal for learning.

Note. As SAS itself is comprehensive, materials given here only serive for illustrative purpose. We do not aim to create a "new standard" for data input and output. However, we believe the implementation will be very useful to researchers in their own work.
