library(dplyr)
library(biomaRt)

rm(list=ls())
setwd('/home/andrew/Projects/gpcr_gene_lists')

# Extract data from Guide2pharmacology
g2p <-  read.csv('https://www.guidetopharmacology.org/DATA/targets_and_families.csv',stringsAsFactors = F)
g2p_gpcr_genes <- g2p %>% 
  filter((Type == 'gpcr') & (HGNC.symbol != ""))

print(c('Number of GPCR gene symbols: ',nrow(g2p_gpcr_genes)))

# Remove pseudogenes
target_genes <- g2p_gpcr_genes %>% 
  filter(
    (substring(HGNC.symbol,nchar(HGNC.symbol)) != 'P') & 
    (Human.SwissProt != "")
  ) %>% 
  select(HGNC.symbol,HGNC.name) %>% 
  distinct()
  
pseudogenes <- g2p_gpcr_genes %>% 
  filter(
    (substring(HGNC.symbol,nchar(HGNC.symbol)) == 'P') | 
    (Human.SwissProt == "")
  ) %>% select(HGNC.symbol,HGNC.name)

# Connect to Grch38 biomart to get ensembl ids
ensembl <- useEnsembl(biomart = "ENSEMBL_MART_ENSEMBL", dataset = "hsapiens_gene_ensembl")


target_genes_grch38 <- getBM(
  attributes = c('hgnc_symbol','ensembl_gene_id','gene_biotype','chromosome_name','start_position','end_position'),
  filters = c('hgnc_symbol'),
  values = target_genes$HGNC.symbol,
  mart = ensembl,
  useCache = F
  )
# remove bad chromosomal locations & pseudogenes

target_genes_grch38_filtered <- target_genes_grch38 %>% 
  filter(nchar(chromosome_name) <=2) %>% 
  filter(gene_biotype=='protein_coding') %>% 
  dplyr::select(-gene_biotype) %>% 
  rename(
    ensembl_gene_id_Grch38=ensembl_gene_id,
    chromosome_name_Grch38=chromosome_name,
    start_position_Grch38=start_position,
    end_position_Grch38=end_position
    )

target_genes_grch38_filtered <- target_genes %>% 
  inner_join(target_genes_grch38_filtered,by=c('HGNC.symbol'='hgnc_symbol'))

write.csv(target_genes_grch38_filtered,'data/all_genes/g2p_gpcrs_ensembl_Grch38_position.csv',row.names = F)

# Now connect to Grch37 biomart to get genome locations

ensembl_grch37 <- useEnsembl(biomart = "ENSEMBL_MART_ENSEMBL", dataset = "hsapiens_gene_ensembl",host='grch37.ensembl.org')


target_genes_grch37 <- getBM(
  attributes = c('hgnc_symbol','ensembl_gene_id','gene_biotype','chromosome_name','start_position','end_position'),
  filters = c('ensembl_gene_id'),
  values = target_genes_grch38_filtered$ensembl_gene_id_Grch38,
  mart = ensembl_grch37,
  useCache = F
)

# Again, select only good chromosomes and protein-coding genes

target_genes_grch37_filtered <- target_genes_grch37 %>% 
  filter(nchar(chromosome_name) <=2) %>% 
  filter(gene_biotype=='protein_coding') %>% 
  dplyr::select(-gene_biotype) %>% 
  rename(
    symbol_Grch37=hgnc_symbol,
    ensembl_gene_id_Grch37=ensembl_gene_id,
    chromosome_name_Grch37=chromosome_name,
     start_position_Grch37=start_position,
     end_position_Grch37=end_position)


# join, check discrepancies, and write to file


target_genes_with_ensembl <- inner_join(
  target_genes_grch38_filtered,
  target_genes_grch37_filtered,
  by=c('ensembl_gene_id_Grch38'='ensembl_gene_id_Grch37'),
  keep=T
)

final <- target_genes_with_ensembl$HGNC.symbol
initial <- target_genes$HGNC.symbol
missing <- initial[!initial %in% final]
print(missing)

missing_genes_grch38_filtered <- target_genes_grch38_filtered %>% 
  filter(HGNC.symbol %in% missing)

missing_genes_grch37 <- getBM(
  attributes = c('hgnc_symbol','ensembl_gene_id','gene_biotype','chromosome_name','start_position','end_position'),
  filters = c('hgnc_symbol'),
  values = missing,
  mart = ensembl_grch37,
  useCache = F
)

  

missing_genes_grch37_filtered <- missing_genes_grch37 %>% 
  filter(!is.na(hgnc_symbol)) %>% 
  filter(gene_biotype == 'protein_coding') %>% 
  filter(nchar(chromosome_name) <=2) %>% 
  dplyr::select(-gene_biotype) %>% 
  rename(
    symbol_Grch37=hgnc_symbol,
    ensembl_gene_id_Grch37=ensembl_gene_id,
    chromosome_name_Grch37=chromosome_name,
    start_position_Grch37=start_position,
    end_position_Grch37=end_position)

missing_genes_with_ensembl <- inner_join(
  missing_genes_grch38_filtered, 
  missing_genes_grch37_filtered,
  by=c('HGNC.symbol'='symbol_Grch37'),
  keep=T
)

all_genes_with_ensembl <- rbind(target_genes_with_ensembl, missing_genes_with_ensembl)

write.csv(all_genes_with_ensembl,'data/all_genes/g2p_gpcrs_ensembl_positions.csv',row.names = F)

possible_pseudogenes <- target_genes %>% 
  select(HGNC.symbol,HGNC.name) %>% 
  left_join(all_genes_with_ensembl,by='HGNC.symbol',suffix=c("","_")) %>% 
  filter(is.na(ensembl_gene_id_Grch37)) %>% 
  select(HGNC.symbol,HGNC.name)

all_pseudogenes <- rbind(pseudogenes,possible_pseudogenes)
write.csv(all_pseudogenes,'data/all_genes/g2p_gpcrs_pseudogenes.csv',row.names = F)

all_genes <-rbind(
  select(all_genes_with_ensembl,HGNC.symbol,HGNC.name) %>% mutate(is_pseudogene='No'),
  all_pseudogenes %>% mutate(is_pseudogene='Yes')
)
write.csv(all_genes,'data/all_genes/g2p_gpcrs_all.csv')

