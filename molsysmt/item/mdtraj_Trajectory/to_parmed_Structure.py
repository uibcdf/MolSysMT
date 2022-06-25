from molsysmt._private.digestion import digest_item, digest_atom_indices, digest_structure_indices

def to_parmed_Structure(item, atom_indices='all', structure_indices='all', check=True):

    if check:

        digest_item(item, 'mdtraj.Trajectory')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    from . import to_openmm_Topology
    from ..openmm_Topology import to_parmed_Structures as openmm_Topology_to_parmed_Structures

    tmp_item = to_openmm_Topology(item, atom_indices=atom_indices, check=False)
    tmp_item = openmm_Topology_to_parmed_Structures(tmp_item, check=False)

    return tmp_item
