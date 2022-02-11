import pandas as pd
ot_drugs = []
with open('opentargets_drugs_20.06.json','r') as fid:
    for i, line in enumerate(fid):
        OT_drug = json.loads(line)
        output = dict(
            target_gene_symbol = OT_drug['target']['gene_info']['symbol'],
            drug_name = OT_drug['drug']['molecule_name'],
            drug_chembl_id = OT_drug['drug']['id'],
            disease_name = OT_drug['disease']['efo_info']['label'],
            disease_id = OT_drug['disease']['id']
        )
        ot_drugs.append(output)

        if i > 1000:
            break

ot_drugs = pd.concat(ot_drugs)
ot_drugs.to_csv('OT_drugs_extracted.csv')