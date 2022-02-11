# %%
import pandas as pd

impc_phenotype_hits = pd.read_csv('data/model_organisms/impc_phenotypeHitsPerGene.csv')
impc_phenotype_hits.columns = ['MGI_symbol','MGI_id','n_phenotype_hits','phenotype_hits']
impc_phenotype_hits = impc_phenotype_hits[~impc_phenotype_hits.MGI_symbol.isna()]
impc_phenotype_hits['phenotype_hits'] = impc_phenotype_hits.phenotype_hits.str.split('::').fillna("").apply(list)
impc_phenotype_hits['lethal_phenotype_hits'] = impc_phenotype_hits.phenotype_hits.apply(lambda hits: [hit for hit in hits if 'lethal' in hit])

# merge with GuideToPharm targets to link to human genes
target_families = pd.read_csv('http://www.guidetopharmacology.org/DATA/targets_and_families.csv')
target_families = target_families[['Type','HGNC symbol','MGI symbol']]
target_families.columns = ['Type','HGNC_symbol','MGI_symbol']
impc_phenotype_hits = target_families.merge(impc_phenotype_hits,on='MGI_symbol')
impc_phenotype_hits[impc_phenotype_hits.Type == 'gpcr']
impc_phenotype_hits = impc_phenotype_hits.drop(columns=['Type','n_phenotype_hits'])
impc_phenotype_hits.to_csv('lists/gpcr_mouse_phenotypes.csv')


