# GPCR-focused gene annotations

## Overview
This repository contains lists of genes with particular phenotypic associations. It is based on the Macarthur lab's resource, but has been updated and to focus on GPCR genes.

| List | Count | Description | Please cite |
| ---- | ---- | ---- | ---- |
| [Universe](lists/universe.tsv) | 19,208 | Approved symbols for 19,208 protein-coding genes. This list is the "universe" of which all subsequent lists are subsets. | "HUGO Gene Nomenclature Committee at the European Bioinformatics Institute" (http://www.genenames.org/) |
| [GPCR genes by family](lists/targets.tsv) | 392+ | Non-olfactory protein-coding GPCR genes from GuideToPharmacology with families from GPCRdb |  [[UniProt Consortium 2018]] [[Alexander 2017] & [Harding 2018]]|
| [Approved or investigational drug targets](lists/drug_targets.tsv) | 385 | Genes whose protein products are known to be the mechanistic targets of FDA-approved drugs (*updated 2018-09-13*). For details on the exact criteria we used for inclusion in this list, see [src/drug_targets.py](src/drug_targets.py)  | See [drugbank.ca/about](http://www.drugbank.ca/about). Please cite [[Law 2014], [Knox 2011], [Wishart 2008], [Wishart 2006], and/or [Wishart 2018]].  |
| [Genetic disease genes](lists/disease_genes.tsv) | 2000+ | Data from OMIM and with additional curation from the union of the Berg and Blekhman dominant & recessive lists | [[Blekhman 2008], [Berg 2013]] [[Rehm 2015]]|
| [Essential in mice](lists/mgi_essential.tsv) | 2,454 | Genes where homozygous knockout in mice results in pre-, peri- or post-natal lethality. The mouse phenotypes were reported by Jackson Labs [[Blake 2011]], then essential gene list was extracted via manual review of phenotypes by [[Georgi 2013]], and the essential/non-essential flag was put into dbNSFP [[Liu 2013]]. We extracted the genes from dbNSFP. Also need to add IMPC if this is different?| [[Blake 2011], [Georgi 2013], and [Liu 2013]] |
| [Essential in human cells](lists/mgi_essential.tsv) | 2,454 | Genes where homozygous knockout in mice results in pre-, peri- or post-natal lethality. The mouse phenotypes were reported by Jackson Labs [[Blake 2011]], then essential gene list was extracted via manual review of phenotypes by [[Georgi 2013]], and the essential/non-essential flag was put into dbNSFP [[Liu 2013]]. We extracted the genes from dbNSFP. Also need to add IMPC if this is different?| [[Blake 2011], [Georgi 2013], and [Liu 2013]] |

## Methods
* Human GPCR genes were extracted from Guide To Pharmacology and annotated with GPCRdb family slugs
* GPCR-linked genetic disease were extracted from the work of Schoeneberg (2021) and modes of inheritance were assigned based on OMIM data
* GPCR drug targets were extracted from drugbank
* GPCRs with associated mouse phenotypes were extracted from IMPC data

## Potential addons
* Drug targets from [[Nelson 2012], [Russ & Lampel 2005]]
* Add Olfactory receptors from Mainland 2015's [data release](http://files.figshare.com/1816348/Receptors.tsv); Kinases; Nuclear receptors [[Hunter 2000], [Manning 2002], [Miranda-Saavedra & Barton 2007]] 
* Also possibly include Natural product targets from [[Dancik 2010]]
* Genes deemed essential in multiple cultured cell lines based on shRNA and CRISPR/Cas screening data [[Hart 2014], [Hart 2017]]
* add ClinVar [[Landrum 2014]] later  & Genes with sufficient evidence for dosage pathogenicity (level 3) as determined by the ClinGen Dosage Sensitivity Map as of Sep 13, 2018 


The files required are 
- `drugbank.xml` - this contains the whole DrugBank database in XML form and can be downloaded from the drugbank website
- `opentargets_drugs_20.06.json` - this contains all opentargets evidence relating to drugs. it can be downloaded from `ftp.ebi.ac.uk/pub/databases/opentargets/platform/21.11/output/etl/json/molecule`
- `ATC.csv` - this contains definitions for all WHO ATC codes. It can be downloaded from `https://bioportal.bioontology.org/ontologies/ATC/`
- `guidetopharm_drugs.csv` - this contains all approved drugs in the GuideToPharmacology database and their primary targets. It can be downloaded from `https://www.guidetopharmacology.org/DATA/approved_drug_primary_target_interactions.csv`
- `guidetopharm_targets.csv` - this contains all targets in the GuideToPharmacology database, annotated with families. It can be downloaded from `https://www.guidetopharmacology.org/DATA/targets_and_families.csv`

[Dancik 2010]: http://www.ncbi.nlm.nih.gov/pubmed/20565092 "Dancík V, Seiler KP, Young DW, Schreiber SL, Clemons PA. Distinct biological network properties between the targets of natural products and disease genes. J Am Chem Soc. 2010 Jul 14;132(27):9259-61. doi: 10.1021/ja102798t. PubMed PMID: 20565092; PubMed Central PMCID: PMC2898216."

[Pawson 2014]: http://www.ncbi.nlm.nih.gov/pubmed/24234439 "Pawson AJ, Sharman JL, Benson HE, Faccenda E, Alexander SP, Buneman OP, Davenport AP, McGrath JC, Peters JA, Southan C, Spedding M, Yu W, Harmar AJ; NC-IUPHAR. The IUPHAR/BPS Guide to PHARMACOLOGY: an expert-driven knowledgebase of drug targets and their ligands. Nucleic Acids Res. 2014 Jan;42(Database issue):D1098-106. doi: 10.1093/nar/gkt1143. Epub 2013 Nov 14. PubMed PMID: 24234439; PubMed Central PMCID: PMC3965070."

[Miranda-Saavedra & Barton 2007]: http://www.ncbi.nlm.nih.gov/pubmed/17557329 "Miranda-Saavedra D, Barton GJ. Classification and functional annotation of eukaryotic protein kinases. Proteins. 2007 Sep 1;68(4):893-914. PubMed PMID: 17557329."

[Manning 2002]: http://www.ncbi.nlm.nih.gov/pubmed/12471243 "Manning G, Whyte DB, Martinez R, Hunter T, Sudarsanam S. The protein kinase complement of the human genome. Science. 2002 Dec 6;298(5600):1912-34. Review. PubMed PMID: 12471243."

[Hunter 2000]: http://www.ncbi.nlm.nih.gov/pubmed/10647936 "Hunter T. Signaling--2000 and beyond. Cell. 2000 Jan 7;100(1):113-27. Review.  PubMed PMID: 10647936."

[Law 2014]: http://www.ncbi.nlm.nih.gov/pubmed/24203711 "Law V, Knox C, Djoumbou Y, Jewison T, Guo AC, Liu Y, Maciejewski A, Arndt D, Wilson M, Neveu V, Tang A, Gabriel G, Ly C, Adamjee S, Dame ZT, Han B, Zhou Y, Wishart DS. DrugBank 4.0: shedding new light on drug metabolism. Nucleic Acids Res. 2014 Jan;42(Database issue):D1091-7. doi: 10.1093/nar/gkt1068. Epub 2013 Nov 6. PubMed PMID: 24203711; PubMed Central PMCID: PMC3965102."

[Knox 2011]: http://www.ncbi.nlm.nih.gov/pubmed/21059682 "Knox C, Law V, Jewison T, Liu P, Ly S, Frolkis A, Pon A, Banco K, Mak C, Neveu V, Djoumbou Y, Eisner R, Guo AC, Wishart DS. DrugBank 3.0: a comprehensive resource for 'omics' research on drugs. Nucleic Acids Res. 2011 Jan;39(Database issue):D1035-41. doi: 10.1093/nar/gkq1126. Epub 2010 Nov 8. PubMed PMID: 21059682; PubMed Central PMCID: PMC3013709."

[Wishart 2008]: http://www.ncbi.nlm.nih.gov/pubmed/18048412 "Wishart DS, Knox C, Guo AC, Cheng D, Shrivastava S, Tzur D, Gautam B, Hassanali M. DrugBank: a knowledgebase for drugs, drug actions and drug targets.  Nucleic Acids Res. 2008 Jan;36(Database issue):D901-6. Epub 2007 Nov 29. PubMed PMID: 18048412; PubMed Central PMCID: PMC2238889."

[Wishart 2006]: http://www.ncbi.nlm.nih.gov/pubmed/16381955 "Wishart DS, Knox C, Guo AC, Shrivastava S, Hassanali M, Stothard P, Chang Z, Woolsey J. DrugBank: a comprehensive resource for in silico drug discovery and exploration. Nucleic Acids Res. 2006 Jan 1;34(Database issue):D668-72. PubMed PMID: 16381955; PubMed Central PMCID: PMC1347430."

[Blekhman 2008]: http://www.ncbi.nlm.nih.gov/pubmed/18571414 "Blekhman R, Man O, Herrmann L, Boyko AR, Indap A, Kosiol C, Bustamante CD, Teshima KM, Przeworski M. Natural selection on genes that underlie human disease  susceptibility. Curr Biol. 2008 Jun 24;18(12):883-9. doi: 10.1016/j.cub.2008.04.074. PubMed PMID: 18571414; PubMed Central PMCID: PMC2474766."

[Berg 2013]: http://www.ncbi.nlm.nih.gov/pubmed/22995991 "Berg JS, Adams M, Nassar N, Bizon C, Lee K, Schmitt CP, Wilhelmsen KC, Evans JP. An informatics approach to analyzing the incidentalome. Genet Med. 2013 Jan;15(1):36-44. doi: 10.1038/gim.2012.112. Epub 2012 Sep 20. PubMed PMID: 22995991; PubMed Central PMCID: PMC3538953."

[Nelson 2012]: http://www.ncbi.nlm.nih.gov/pubmed/22604722 "Nelson MR, Wegmann D, Ehm MG, Kessner D, St Jean P, Verzilli C, Shen J, Tang Z, Bacanu SA, Fraser D, Warren L, Aponte J, Zawistowski M, Liu X, Zhang H, Zhang  Y, Li J, Li Y, Li L, Woollard P, Topp S, Hall MD, Nangle K, Wang J, Abecasis G, Cardon LR, Zöllner S, Whittaker JC, Chissoe SL, Novembre J, Mooser V. An abundance of rare functional variants in 202 drug target genes sequenced in 14,002 people. Science. 2012 Jul 6;337(6090):100-4. doi: 10.1126/science.1217876. Epub 2012 May 17. PubMed PMID: 22604722; PubMed Central PMCID: PMC4319976."

[Russ & Lampel 2005]: http://www.ncbi.nlm.nih.gov/pubmed/16376820 "Russ AP, Lampel S. The druggable genome: an update. Drug Discov Today. 2005 Dec;10(23-24):1607-10. PubMed PMID: 16376820."

[Hart 2014]: http://www.ncbi.nlm.nih.gov/pubmed/24987113 "Hart T, Brown KR, Sircoulomb F, Rottapel R, Moffat J. Measuring error rates in genomic perturbation screens: gold standards for human functional genomics. Mol Syst Biol. 2014 Jul 1;10:733. doi: 10.15252/msb.20145216. PubMed PMID: 24987113;  PubMed Central PMCID: PMC4299491."

[Hart 2017]: http://www.g3journal.org/content/7/8/2719 "HART, Traver, et al. Evaluation and design of genome-wide CRISPR/SpCas9 knockout screens. G3: Genes, Genomes, Genetics, 2017, g3. 117.041277. doi: 10.1534/g3.117.041277. PMID: 28655737 PMCID: PMC5555476"


[Welter 2014]: http://www.ncbi.nlm.nih.gov/pubmed/24316577 "Welter D, MacArthur J, Morales J, Burdett T, Hall P, Junkins H, Klemm A, Flicek P, Manolio T, Hindorff L, Parkinson H. The NHGRI GWAS Catalog, a curated resource of SNP-trait associations. Nucleic Acids Res. 2014 Jan;42(Database issue):D1001-6. doi: 10.1093/nar/gkt1229. Epub 2013 Dec 6. PubMed PMID: 24316577; PubMed Central PMCID: PMC3965119."

[Georgi 2013]: http://www.ncbi.nlm.nih.gov/pubmed/23675308 "Georgi B, Voight BF, Bućan M. From mouse to human: evolutionary genomics analysis of human orthologs of essential genes. PLoS Genet. 2013 May;9(5):e1003484. doi: 10.1371/journal.pgen.1003484. Epub 2013 May 9. PubMed PMID: 23675308; PubMed Central PMCID: PMC3649967."

[Blake 2011]: http://www.ncbi.nlm.nih.gov/pubmed/21051359 "Blake JA, Bult CJ, Kadin JA, Richardson JE, Eppig JT; Mouse Genome Database Group. The Mouse Genome Database (MGD): premier model organism resource for mammalian genomics and genetics. Nucleic Acids Res. 2011 Jan;39(Database issue):D842-8. doi: 10.1093/nar/gkq1008. Epub 2010 Nov 3. PubMed PMID: 21051359;  PubMed Central PMCID: PMC3013640."

[Liu 2013]: http://www.ncbi.nlm.nih.gov/pubmed/23843252 "Liu X, Jian X, Boerwinkle E. dbNSFP v2.0: a database of human non-synonymous SNVs and their functional predictions and annotations. Hum Mutat. 2013 Sep;34(9):E2393-402. doi: 10.1002/humu.22376. Epub 2013 Jul 10. PubMed PMID: 23843252; PubMed Central PMCID: PMC4109890."

[Wood 2005]: http://www.ncbi.nlm.nih.gov/pubmed/15922366 "Human DNA repair genes, 2005. Wood RD1, Mitchell M, Lindahl T"

[Kang 2012]: http://www.ncbi.nlm.nih.gov/pubmed/22505474 "A DNA repair pathway-focused score for prediction of outcomes in ovarian cancer treated with platinum-based chemotherapy."

[Mainland 2015]: http://www.nature.com/articles/sdata20152 "Joel D Mainland, Yun R Li, Ting Zhou, Wen Ling L Liu & Hiroaki Matsunami. Human olfactory receptor responses to odorants. Scientific Data 2, Article number: 150002 (2015) ​Received 22 April 2014 Accepted 10 December 2014 Published online 03 February 2015 doi:10.1038/sdata.2015.2"

[Rehm 2015]: https://www.ncbi.nlm.nih.gov/pubmed/26014595/ "Rehm HL, Berg JS, Brooks LD, Bustamante CD, Evans JP, Landrum MJ, Ledbetter DH, Maglott DR, Martin CL, Nussbaum RL, Plon SE, Ramos EM, Sherry ST, Watson MS;  ClinGen. ClinGen--the Clinical Genome Resource. N Engl J Med. 2015 Jun 4;372(23):2235-42. doi: 10.1056/NEJMsr1406261. Epub 2015 May 27. PubMed PMID: 26014595; PubMed Central PMCID: PMC4474187."

[Landrum 2014]: http://www.ncbi.nlm.nih.gov/pubmed/24234437 "Landrum MJ, Lee JM, Riley GR, Jang W, Rubinstein WS, Church DM, Maglott DR. ClinVar: public archive of relationships among sequence variation and human phenotype. Nucleic Acids Res. 2014 Jan;42(Database issue):D980-5. doi: 10.1093/nar/gkt1113. Epub 2013 Nov 14. PubMed PMID: 24234437; PubMed Central PMCID: PMC3965032."

[Lek 2016]: https://www.ncbi.nlm.nih.gov/pubmed/27535533/ "Lek M, Karczewski KJ, Minikel EV, Samocha KE, Banks E, Fennell T, O'Donnell-Luria AH, Ware JS, Hill AJ, Cummings BB, Tukiainen T, Birnbaum DP, Kosmicki JA, Duncan LE, Estrada K, Zhao F, Zou J, Pierce-Hoffman E, Berghout J, Cooper DN, Deflaux N, DePristo M, Do R, Flannick J, Fromer M, Gauthier L, Goldstein J, Gupta N, Howrigan D, Kiezun A, Kurki MI, Moonshine AL, Natarajan P, Orozco L, Peloso GM, Poplin R, Rivas MA, Ruano-Rubio V, Rose SA, Ruderfer DM, Shakir K, Stenson PD, Stevens C, Thomas BP, Tiao G, Tusie-Luna MT, Weisburd B, Won HH, Yu D, Altshuler DM, Ardissino D, Boehnke M, Danesh J, Donnelly S, Elosua R, Florez JC, Gabriel SB, Getz G, Glatt SJ, Hultman CM, Kathiresan S, Laakso M, McCarroll S, McCarthy MI, McGovern D, McPherson R, Neale BM, Palotie A, Purcell SM, Saleheen D, Scharf JM, Sklar P, Sullivan PF, Tuomilehto J, Tsuang MT, Watkins HC, Wilson JG, Daly MJ, MacArthur DG; Exome Aggregation Consortium. Analysis of protein-coding genetic variation in 60,706 humans. Nature. 2016 Aug 18;536(7616):285-91. doi: 10.1038/nature19057. PubMed PMID: 27535533; PubMed Central PMCID: PMC5018207."

[UniProt Consortium 2017]: https://www.ncbi.nlm.nih.gov/pubmed/27899622 "The UniProt Consortium. UniProt: the universal protein knowledgebase. Nucleic Acids Res. 2017 Jan 4;45(D1):D158-D169. doi: 10.1093/nar/gkw1099. Epub 2016 Nov 29. PubMed PMID: 27899622; PubMed Central PMCID: PMC5210571."

[Kalia 2017]: https://www.ncbi.nlm.nih.gov/pubmed/27854360 "Kalia SS, Adelman K2, Bale SJ, Chung WK, Eng C, Evans JP, Herman GE, Hufnagel SB, Klein TE, Korf BR, McKelvey KD, Ormond KE, Richards CS, Vlangos CN, Watson M, Martin CL, Miller DT; Recommendations for reporting of secondary findings in clinical exome and genome sequencing, 2016 update (ACMG SF v2.0): a policy statement of the American College of Medical Genetics and Genomics. Genet Med. 2017 Feb;19(2):249-255. doi: 10.1038/gim.2016.190. Epub 2016 Nov 17."

[Alexander 2017]: https://www.ncbi.nlm.nih.gov/pubmed/29055040 "Alexander SP, Christopoulos A, Davenport AP, Kelly E, Marrion NV, Peters JA, Faccenda E, Harding SD, Pawson AJ, Sharman JL, Southan C, Davies JA; CGTP Collaborators. THE CONCISE GUIDE TO PHARMACOLOGY 2017/18: G protein-coupled receptors. Br J Pharmacol. 2017 Dec;174 Suppl 1:S17-S129. doi: 10.1111/bph.13878. PubMed PMID: 29055040; PubMed Central PMCID: PMC5650667."

[MacArthur 2017]: https://www.ncbi.nlm.nih.gov/pubmed/27899670/ "MacArthur J, Bowler E, Cerezo M, Gil L, Hall P, Hastings E, Junkins H, McMahon A, Milano A, Morales J, Pendlington ZM, Welter D, Burdett T, Hindorff L, Flicek P, Cunningham F, Parkinson H. The new NHGRI-EBI Catalog of published genome-wide  association studies (GWAS Catalog). Nucleic Acids Res. 2017 Jan 4;45(D1):D896-D901. doi: 10.1093/nar/gkw1133. Epub 2016 Nov 29. PubMed PMID: 27899670; PubMed Central PMCID: PMC5210590."

[Harding 2018]: https://www.ncbi.nlm.nih.gov/pubmed/29149325 "Harding SD, Sharman JL, Faccenda E, Southan C, Pawson AJ, Ireland S, Gray AJG, Bruce L, Alexander SPH, Anderton S, Bryant C, Davenport AP, Doerig C, Fabbro D, Levi-Schaffer F, Spedding M, Davies JA; NC-IUPHAR. The IUPHAR/BPS Guide to PHARMACOLOGY in 2018: updates and expansion to encompass the new guide to IMMUNOPHARMACOLOGY. Nucleic Acids Res. 2018 Jan 4;46(D1):D1091-D1106. doi: 10.1093/nar/gkx1121. PubMed PMID: 29149325; PubMed Central PMCID: PMC5753190."

[Wishart 2018]: https://www.ncbi.nlm.nih.gov/pubmed/29126136/ "Wishart DS, Feunang YD, Guo AC, Lo EJ, Marcu A, Grant JR, Sajed T, Johnson D,  Li C, Sayeeda Z, Assempour N, Iynkkaran I, Liu Y, Maciejewski A, Gale N, Wilson A, Chin L, Cummings R, Le D, Pon A, Knox C, Wilson M. DrugBank 5.0: a major update to the DrugBank database for 2018. Nucleic Acids Res. 2018 Jan 4;46(D1):D1074-D1082. doi: 10.1093/nar/gkx1037. PubMed PMID: 29126136; PubMed Central PMCID: PMC5753335."

[UniProt Consortium 2018]: https://www.ncbi.nlm.nih.gov/pubmed/29425356 "UniProt Consortium T. UniProt: the universal protein knowledgebase. Nucleic Acids Res. 2018 Mar 16;46(5):2699. doi: 10.1093/nar/gky092. PubMed PMID: 29425356; PubMed Central PMCID: PMC5861450."
