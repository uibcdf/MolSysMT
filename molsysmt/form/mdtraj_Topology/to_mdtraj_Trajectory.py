from molsysmt._private.digestion import digest

@digest(form='mdtraj.Topology')
def to_mdtraj_Trajectory(item, atom_indices='all', coordinates=None, box=None, skip_digestion=False):

    from mdtraj.core.trajectory import Trajectory
    from . import extract

    tmp_item = extract(item, atom_indices=atom_indices, skip_digestion=True)
    tmp_item = Trajectory(coordinates, item)

    return tmp_item

