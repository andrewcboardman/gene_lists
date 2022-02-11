options(stringsAsFactors=F)
#setwd('~/d/sci/src/gene_lists')

# Get list of GPCR targets from Guide To Pharamacology
targets_and_families_path <- 'data/target_genes/targets_and_families.csv'
if (!file.exists(targets_and_families_path)) {
    download.file(
        url='http://www.guidetopharmacology.org/DATA/targets_and_families.csv',
        destfile=targets_and_families_path
        )
}
data = read.table(targets_and_families_path,sep=',',quote='"',header=T)
gpcrs = subset(data,Type == "gpcr",c(Target.id,HGNC.symbol,HGNC.name,Human.SwissProt))
#fGet families for GPCR targets from GPCRdb
GPCRdb_proteins = read.table('data/target_genes/GPCRdb_proteins.csv',sep=',',header=T)
GPCRdb_proteins = subset(GPCRdb_proteins,species=="Homo sapiens",c(uniprot_name,uniprot_accession,GPCRdb_slug))
gpcr_targets = merge(gpcrs,GPCRdb_proteins,by.x='Human.SwissProt',by.y='uniprot_accession',all=T)
gpcr_targets = subset(gpcr_targets,Human.SwissProt!="")
colnames(gpcr_targets) = c(
    "UniProt_accession",
    "Guide2Pharm_target_id",
    "HGNC_symbol",
    "HGNC_name",
    "UniProt_name",
    "GPCRdb_slug"
)
gpcr_targets = gpcr_targets[c(
    "HGNC_symbol",
    "HGNC_name",
    "UniProt_accession",
    "UniProt_name",
    "Guide2Pharm_target_id",    
    "GPCRdb_slug"
)]
gpcr_targets = gpcr_targets[order(gpcr_targets$HGNC_symbol),]
write.csv(gpcr_targets,'lists/gpcrs.csv')