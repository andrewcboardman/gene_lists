import pandas as pd
import json
import xml.etree.ElementTree as ET
import re
from copy import deepcopy

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
output.to_csv('lists/drug_targets.tsv',sep='\t')