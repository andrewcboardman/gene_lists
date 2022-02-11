import os
import pandas as pd
import numpy as np
import json
import xml.etree.ElementTree as ET
import re
from copy import deepcopy

def parse_drugbank():
    ip = ET.iterparse('drugbank.xml', events=("start", "end"))
    max_lines = 100000000

    path = []
    template = {'target_ids':[],'target_names':[],'modes_of_action':[]}
    outputs = []

    strip_tag = lambda tag: re.sub('{http://www.drugbank.ca}','',tag)

    for i, (event, elem) in enumerate(ip):
        if event == 'start':
            path.append(strip_tag(elem.tag))
        
            if path == ['drugbank','drug']:
                output_ = {}
            elif path[2:] == ['groups']:
                output_['groups'] = []
            elif path[2:] == ['atc-codes']:
                output_['atc-codes'] = []
            elif path[2:] == ['targets']:
                output_['targets']  = []
            elif path[2:] == ['targets','target']:
                output_['targets'].append({})
            elif path[2:] == ['targets','target','actions']:
                output_['targets'][-1]['actions'] = []
            

        if event == 'end':
            
            if path[2:] == ['drugbank-id'] and 'primary' in elem.attrib.keys():
                output_['drugbank_id'] = elem.text           
            if path[2:] == ['name']:
                output_['name'] = elem.text
            if path[2:] == ['groups','group']:
                output_['groups'].append(elem.text)
            if path[2:] == ['atc-codes','atc-code']:
                output_['atc-codes'].append(elem.attrib['code'])
            if path[2:] == ['targets','target','id']:
                output_['targets'][-1]['target_id'] = elem.text
            if path[2:] == ['targets','target','name']:
                output_['targets'][-1]['target_name'] = elem.text
            if path[2:] == ['targets','target','polypeptide']:
                output_['targets'][-1]['uniprot_id'] = elem.attrib['id']
            if path[2:] == ['targets','target','actions','action']:
                output_['targets'][-1]['actions'].append(elem.text)
            if path[2:] == ['targets','target','known-action']:
                output_['targets'][-1]['known-action'] = elem.text

            if path == ['drugbank','drug']:
                output_['type'] = elem.attrib['type']
                outputs.append(deepcopy(output_))
            path.pop()
        if i > max_lines:
            break

    output = pd.DataFrame(outputs)
    output['groups'] = output.groups.map(json.dumps)
    output['atc-codes'] = output['atc-codes'].map(json.dumps)
    output['targets'] = output.targets.map(json.dumps)
    return output

def collapse_drugbank_targets(drugbank_drugs):
    drugbank_drugs['groups'] = drugbank_drugs.groups.map(json.loads)
    drugbank_drugs['atc-codes'] = drugbank_drugs['atc-codes'].map(json.loads)
    drugbank_drugs['targets'] = drugbank_drugs.targets.map(json.loads)

    # Explode by target-drug pair
    drugbank_drug_targets = drugbank_drugs.explode('targets')
    drugbank_drug_targets = drugbank_drug_targets[~drugbank_drug_targets.targets.isna()]
    drugbank_drug_targets = drugbank_drug_targets.reset_index().drop(columns='index')
    target_info = pd.json_normalize(drugbank_drug_targets.targets)
    drugbank_drug_targets = pd.concat((drugbank_drug_targets.drop(columns='targets'),target_info),axis=1)
    drugbank_drug_targets = drugbank_drug_targets.rename(columns={'uniprot_id':'target_uniprot_id'})

    # Filter by known action
    check_actions = drugbank_drug_targets.actions.map(lambda actions: len(actions) > 0) & \
        (drugbank_drug_targets['known-action'] == 'yes')
    drugbank_drug_targets = drugbank_drug_targets[check_actions]
    drugbank_drug_targets = drugbank_drug_targets[['name','groups','atc-codes','type','actions','target_uniprot_id']]
    drugbank_drug_targets.columns = ['drug_name','approval_status_groups','atc-codes','drug_type','actions','target_uniprot_id']

    # Filter by approval
    is_approved = drugbank_drug_targets.approval_status_groups.map(lambda groups: set(['approved']).issubset(groups))
    is_investigational = drugbank_drug_targets.approval_status_groups.map(lambda groups: set(['investigational']).issubset(groups))
    is_nutraceutical = drugbank_drug_targets.approval_status_groups.map(lambda groups: set(['nutraceutical']).issubset(groups))
    drugbank_drug_targets['approval_status'] = np.select(
        [is_approved & ~is_nutraceutical, is_investigational & ~is_approved & ~is_nutraceutical],
        ['approved','investigational'], default='other' 
    )
    drugbank_drug_targets = drugbank_drug_targets.drop(columns='approval_status_groups')
    drugbank_drug_targets = drugbank_drug_targets[drugbank_drug_targets.approval_status.isin(('approved','investigational'))]

    atc = pd.read_csv('data/drug_targets/ATC.csv')
    atc = atc[['Preferred Label','Class ID','ATC LEVEL']]
    atc.columns = ['label','code','level']
    atc['code'] = atc.code.apply(lambda x: x.split('/')[-1])
    top_level_atc = atc[atc['level'] == 1]
    top_level_atc_dict = dict(zip(top_level_atc.code, top_level_atc.label))
    bottom_level_atc = atc[atc['level'] == 5]
    bottom_level_atc_dict = dict(zip(bottom_level_atc.code, bottom_level_atc.label))

    drugbank_drug_targets['atc_disease_areas'] = drugbank_drug_targets['atc-codes'].map(lambda x: list(set([top_level_atc_dict[x_[0]] for x_ in x])))
    #drugbank_drug_targets['atc_diseases'] = drugbank_drug_targets['atc-codes'].map(lambda x: [bottom_level_atc_dict[x_] for x_ in x])

    drugbank_drug_targets['drug'] = drugbank_drug_targets.apply(lambda x: {
        'name':x.drug_name, 
        'type':x.drug_type, 
        'actions':x.actions,
        'atc_codes':x['atc-codes'],
        'disease_areas':x['atc_disease_areas'],
        'approval_status':x.approval_status
        },axis=1)
    drugbank_targets = drugbank_drug_targets.groupby('target_uniprot_id').agg({'drug':lambda x: json.dumps(list(x))}).reset_index()
    drugbank_targets.columns = ['UniProt_accession','drugs']
    return drugbank_targets


def main():
    if not os.path.isfile('data/drug_targets/drugbank_extracted.csv'):
        drugbank_drugs = parse_drugbank()
        drugbank_drugs.to_csv('data/drug_targets/drugbank_extracted.csv')

    
    drugbank_drugs = pd.read_csv('data/drug_targets/drugbank_extracted.csv',index_col=0)
    drugbank_drug_targets = collapse_drugbank_targets(drugbank_drugs)
    drugbank_drug_targets.to_csv('data/drug_targets/drugbank_drug_targets.csv')

    gpcrs = pd.read_csv('lists/gpcrs.csv',index_col=0)
    drugbank_gpcr_drug_targets = gpcrs.merge(drugbank_drug_targets,on='UniProt_accession')
    drugbank_gpcr_drug_targets.to_csv('lists/gpcr_drug_targets.csv')

if __name__ == '__main__':
    main()

    
# output.to_csv('lists/drug_targets.tsv',sep='\t')


