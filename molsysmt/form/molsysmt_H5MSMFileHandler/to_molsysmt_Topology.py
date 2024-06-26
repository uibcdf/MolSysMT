from molsysmt._private.digestion import digest
from molsysmt._private.variables import is_all
import pandas as pd
import numpy as np

@digest(form='molsysmt.H5MSMFileHandler')
def to_molsysmt_Topology(item, atom_indices='all', skip_digestion=False):

    from molsysmt.native import Topology

    topology_ds = item.file['topology']

    tmp_item = Topology()

    # Atoms

    tmp_item.atoms['atom_id']=topology_ds['atoms']['id'][:].astype('int64')
    tmp_item.atoms['atom_type']=topology_ds['atoms']['type'].asstr()[:]
    tmp_item.atoms['atom_name']=topology_ds['atoms']['name'].asstr()[:]
    tmp_item.atoms['group_index']=topology_ds['atoms']['group_index'][:].astype('int64')
    tmp_item.atoms['chain_index']=topology_ds['atoms']['chain_index'][:].astype('int64')

    # Groups

    tmp_item.groups['group_id']=topology_ds['groups']['id'][:].astype('int64')
    tmp_item.groups['group_name']=topology_ds['groups']['name'].asstr()[:]
    tmp_item.groups['group_type']=topology_ds['groups']['type'].asstr()[:]
    tmp_item.groups['component_index']=topology_ds['groups']['component_index'][:].astype('int64')

    # Components

    tmp_item.components['component_id']=topology_ds['components']['id'][:].astype('int64')
    tmp_item.components['component_name']=topology_ds['components']['name'].asstr()[:]
    tmp_item.components['component_type']=topology_ds['components']['type'].asstr()[:]
    tmp_item.components['molecule_index']=topology_ds['components']['molecule_index'][:].astype('int64')

    # Molecules

    tmp_item.molecules['molecule_id']=topology_ds['molecules']['id'][:].astype('int64')
    tmp_item.molecules['molecule_name']=topology_ds['molecules']['name'].asstr()[:]
    tmp_item.molecules['molecule_type']=topology_ds['molecules']['type'].asstr()[:]
    tmp_item.molecules['entity_index']=topology_ds['molecules']['entity_index'][:].astype('int64')

    # Entities

    tmp_item.entities['entity_id']=topology_ds['entities']['id'][:].astype('int64')
    tmp_item.entities['entity_name']=topology_ds['entities']['name'].asstr()[:]
    tmp_item.entities['entity_type']=topology_ds['entities']['type'].asstr()[:]

    # Chains
    tmp_item.chains['chain_id']=topology_ds['chains']['id'][:].astype('int64')
    tmp_item.chains['chain_name']=topology_ds['chains']['name'].asstr()[:]
    tmp_item.chains['chain_type']=topology_ds['chains']['type'].asstr()[:]

    # Bonds

    if topology_ds['bonds']['type'].size:
        tmp_item.bonds['type']=topology_ds['bonds']['type'].asstr()[:]
    else:
        tmp_item.bonds.drop('type', axis=1, inplace=True)
    if topology_ds['bonds']['order'].size:
        tmp_item.bonds['order']=topology_ds['bonds']['order'].asstr()[:]
    else:
        tmp_item.bonds.drop('order', axis=1, inplace=True)

    tmp_item.bonds['atom1_index']=topology_ds['bonds']['atom1_index'][:].astype('int64')
    tmp_item.bonds['atom2_index']=topology_ds['bonds']['atom2_index'][:].astype('int64')

    if not is_all(atom_indices):
        tmp_item = tmp_item.extract(atom_indices=atom_indices, skip_digestion=True)

    return tmp_item

