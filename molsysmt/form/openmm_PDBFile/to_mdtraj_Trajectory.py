from molsysmt._private.exceptions import LibraryNotFoundError
from molsysmt._private.digestion import digest

@digest(form='openmm.PDBFile')
def to_mdtraj_Trajectory(item, atom_indices='all', skip_digestion=False):

    from .to_mdtraj_Topology import to_mdtraj_Topology
    from .get import get_coordinates_from_atom

    try:
        from mdtraj.core.trajectory import Trajectory as mdtraj_Trajectory
    except:
        raise LibraryNotFoundError()

    topology = to_mdtraj_Topology(item, atom_indices=atom_indices, skip_digestion=True)
    coordinates = get_coordinates_from_atom(item, indices=atom_indices, structure_indices=structure_indices,
                                            skip_digestion=True)
    tmp_item = mdtraj_Trajectory(positions, topology, skip_digestion=True)

    return tmp_item

