# wget https://files.wwpdb.org/pub/pdb/data/monomers/components.cif

from molsysmt.native import CIFFileHandler
import pickle

handler = CIFFileHandler('components.cif')
cif_entries = handler.parse()

types_dict = {}

for ii in cif_entries:
    jj = cif_entries[ii]['_chem_comp']['type']
    if jj in types_dict:
        types_dict[jj].append(ii)
    else:
        types_dict[jj] = [ii]

types = ['NON-POLYMER', 'non-polymer', 'other']
data = []
for ii in types:
    data += types_dict[ii]
data.remove('UNL')

# quito iones
ions = []
for value in data:
    key = cif_entries[value]
    if key['_chem_comp']['name'].endswith(' ION"') or key['_chem_comp']['name'].endswith(' ion"'):
        ions.append(value)

output = {}

for value in ions:
    
    key = cif_entries[value]

    aux_dict={}

    aux_dict['name']=key['_chem_comp']['name']
    aux_dict['three_letter_code']=key['_chem_comp']['three_letter_code']
    aux_dict['atom_name']=[key['_chem_comp_atom']['atom_id']]
    aux_dict['atom_name'].append(key['_chem_comp_atom']['alt_atom_id'])
    if '_chem_comp_bond' in key:
        bonds = []
        atom_id_1 = key['_chem_comp_bond']['atom_id_1']
        if isinstance(atom_id_1, str):
            atom_id_1=[atom_id_1]
        atom_id_2 = key['_chem_comp_bond']['atom_id_2']
        if isinstance(atom_id_2, str):
            atom_id_2=[atom_id_2]
        for ii,jj in zip(atom_id_1, atom_id_2):
            iii = aux_dict['atom_name'][0].index(ii)
            jjj = aux_dict['atom_name'][0].index(jj)
            if iii>jjj:
                bonds.append([jjj,iii])
            else:
                bonds.append([iii,jjj])
        aux_dict['bonds']=bonds
    else:
        aux_dict['bonds']=[]

    output[value]=aux_dict

#### Extra ####

import json

with open('extra.json', 'r') as fff:
    extra = json.load(fff)

for name in extra.keys():
    if name not in output:
        output[name]=extra[name]
    else:
        output[name]['topology']+=extra[name]['topology']

#### End ####

split_output = {}
for name,value in output.items():
    if name[0] not in split_output:
        split_output[name[0]]={}
    split_output[name[0]][name]=value

import gzip

for file_name, aux_output in split_output.items():
    with gzip.open(file_name+'.pkl.gz', 'wb', compresslevel=9) as fff:
        pickle.dump(aux_output, fff)

with gzip.open('group_names.pkl.gz', 'wb', compresslevel=9) as fff:
        pickle.dump(list(output.keys()), fff)

