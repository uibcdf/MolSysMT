from molsysmt._private.digestion import digest

@digest(form='file:mol2')
def to_mdtraj_Topology(item, atom_indices='all', skip_digestion=False):

    from mdtraj import load_mol2
    from ..mdtraj_Topology import extract as extract_mdtraj_Topology

    tmp_item = load_mol2(item).topology
    tmp_item = extract_mdtraj_Topology(tmp_item, skip_digestion=True)

    return tmp_item

