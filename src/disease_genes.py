
import pandas as pd


gpcr_genetic_diseases = pd.read_csv('data/genetic_diseases/Schoeneberg2021_genetic_diseases_by_gpcr.csv')
# Check where this data comes from
gpcr_genetic_diseases = gpcr_genetic_diseases[['HGNC symbol','Disease associations','Functional_effect','Inheritance_pattern']]
gpcr_genetic_diseases.columns = ['HGNC_symbol','names','action','inheritance']
gpcr_genetic_diseases['disease'] = gpcr_genetic_diseases.apply(lambda x: {'names':x.names,'action':x.action,'inheritance':x.inheritance},axis=1)
gpcr_genetic_diseases = gpcr_genetic_diseases.groupby('HGNC_symbol').agg({'disease':list})
gpcr_genetic_diseases.to_csv('lists/gpcr_genetic_diseases.csv')



