def to_mdtraj_Topology(item, trajectory_item=None, atom_indices='all', frame_indices='all'):

    from mdtraj import Topology
    from mdtraj.core import element

    n_atoms = item.elements.shape[0]

    atom_index_array = item.elements["atom_index"].to_numpy()
    atom_name_array = item.elements["atom_name"].to_numpy()
    atom_id_array = item.elements["atom_id"].to_numpy()
    atom_type_array = item.elements["atom_type"].to_numpy()

    group_index_array = item.elements["group_index"].to_numpy()
    group_name_array = item.elements["group_name"].to_numpy()
    group_id_array = item.elements["group_id"].to_numpy()
    group_type_array = item.elements["group_type"].to_numpy()

    chain_index_array = item.elements["chain_index"].to_numpy()
    chain_name_array = item.elements["chain_name"].to_numpy()
    chain_id_array = item.elements["chain_id"].to_numpy()
    chain_type_array = item.elements["chain_type"].to_numpy()

    bonds_atom1 = item.bonds["atom1_index"].to_numpy()
    bonds_atom2 = item.bonds["atom2_index"].to_numpy()

    tmp_item = Topology()

    former_group_index = -1
    former_chain_index = -1

    list_new_atoms = []

    for ii in range(n_atoms):

        atom_index = atom_index_array[ii]
        atom_name = atom_name_array[ii]
        atom_id = atom_id_array[ii]
        atom_type = atom_type_array[ii]

        group_index = group_index_array[ii]
        chain_index = chain_index_array[ii]

        new_group = (former_group_index!=group_index)
        new_chain = (former_chain_index!=chain_index)

        if new_chain:
            chain = tmp_item.add_chain()
            former_chain_index = chain_index

        if new_group:
            residue_name = group_name_array[ii]
            residue_id = group_id_array[ii]
            residue = tmp_item.add_residue(residue_name, chain, resSeq=str(residue_id))
            former_group_index = group_index

        elem = element.get_by_symbol(atom_type)
        atom = tmp_item.add_atom(atom_name, elem, residue)

        list_new_atoms.append(atom)

    for atom_1, atom_2 in zip(bonds_atom1, bonds_atom2):

        tmp_item.add_bond(list_new_atoms[atom_1], list_new_atoms[atom_2]) # falta bond type and bond order

    return tmp_item

def from_mdtraj_Topology(item, trajectory_item=None, atom_indices='all', frame_indices='all'):

    from molsysmt.native import Topology
    from numpy import empty, array, arange, reshape, where, unique, nan, sort
    from molsysmt.elements.group import name_to_type as group_name_to_group_type

    tmp_item = Topology()

    n_atoms = item.n_atoms

    mdtraj_dataframe, mdtraj_bonds = item.to_dataframe()

    tmp_item.elements["atom_index"] = list(mdtraj_dataframe.index)
    tmp_item.elements["atom_id"] = mdtraj_dataframe["serial"]
    tmp_item.elements["atom_name"] = mdtraj_dataframe["name"]
    tmp_item.elements["atom_type"] = mdtraj_dataframe["element"]

    tmp_item.elements["group_id"] = mdtraj_dataframe["resSeq"]
    tmp_item.elements["group_name"] = mdtraj_dataframe["resName"]

    tmp_item.elements["chain_id"] = mdtraj_dataframe["chainID"]

    del(mdtraj_dataframe)

    group_type_array = empty(n_atoms, dtype=object)

    tmp_item.elements["group_type"] = list(map(group_name_to_group_type,tmp_item["group.name"]))

    bond_atom1 = empty(n_atoms, dtype=int)
    bond_atom2 = empty(n_atoms, dtype=int)

    aux=0
    for mdtraj_bond in mdtraj_bonds:
        bond_atom1=int(mdtraj_bond[0])
        bond_atom2=int(mdtraj_bond[1])
        aux+=1


    tmp_item.bonds['atom1_index']=bond_atom_1
    tmp_item.bonds['atom2_index']=bond_atom_2

    del(bond_atom_1, bond_atom_2)

    group_index_array = empty(n_atoms, dtype=int)
    chain_index_array = empty(n_atoms, dtype=int)

    for atom in item.atoms:
        atom_index = atom.index
        group_index_array[atom_index] = atom.residue.index
        chain_index_array[atom_index] = atom.residue.chain.index

    tmp_item.elements["group_index"] = group_index_array
    tmp_item.elements["chain_index"] = chain_index_array

    del(group_index_array, chain_index_array)

    tmp_item._build_components()
    tmp_item._build_molecules()
    tmp_item._build_entities()

    return tmp_item
