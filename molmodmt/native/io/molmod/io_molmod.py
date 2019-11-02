
#def from_mdtraj_Trajectory(item=None, selection='all', frame_indices='all', syntaxis='MDTraj'):
#
#    from .io_trajectory import from_mdtraj_Trajectory as _from_mdtraj_Trajectory
#    from .io_topology import from_mdtraj_Topology as _from_mdtraj_Topology
#    from .molmod import MolMod as _MolMod
#
#    tmp_molmod_item = _MolMod()
#    tmp_molmod_item.topology = _from_mdtraj_Topology(item.topology, selection=selection,
#                                                     syntaxis='mdtraj')
#    tmp_molmod_item.trajectory = _from_mdtraj_Trajectory(item, selection=selection,
#                                                         frame_indices=frame_indices,
#                                                        syntaxis=syntaxis)
#    tmp_molmod_item.topography = None
#
#    return tmp_molmod_item

#def from_mdtraj(item=None, selection='all', frame_indices='all', syntaxis='MDTraj'):
#
#    return from_mdtraj_Trajectory(item=item, selection=selection, frame_indices=frame_indices, syntaxis=syntaxis)

#def to_mdtraj_Topology(item=None, selection='all', syntaxis='MDTraj'):
#
#    tmp_item = item.topology
#    if selection is not None:
#        from molmodmt import extract as _extract
#        tmp_item = _extract(tmp_item, selection=selection, syntaxis=syntaxis)
#    return tmp_item

#def to_mdtraj_Trajectory(item=None, selection='all', frame_indices='all', syntaxis='MDTraj'):
#
#    from mdtraj import Trajectory as _mdtraj_Trajectory
#    from numpy import ascontiguousarray as _ascontiguousarray
#    tmp_item = _mdtraj_Trajectory(item.trajectory.coordinates,item.topology)
#    tmp_item.unitcell_vectors = _ascontiguousarray(item.trajectory.box)
#    tmp_item.time = _ascontiguousarray(item.trajectory.time)
#
#    return tmp_item

#def to_mdtraj(item=None, selection='all', frame_indices='all', syntaxis='MDTraj'):
#
#    return to_mdtraj_Trajectory(item, selection=selection, frame_indices=frame_indices, syntaxis=syntaxis)

#def from_openmm_Modeller(item=None, selection='all', frame_indices='all', syntaxis='MDTraj'):
#
#    from .io_trajectory import from_openmm_Modeller as trajectory_from_mdtraj_Trajectory
#    from .io_topology import from_openmm_Modeller as topology_from_mdtraj_Topology
#    from .molmod import MolMod as _MolMod
#
#    tmp_item = _MolMod()
#    tmp_item.topology = topology_from_mdtraj_Topology(item, selection=selection, syntaxis='MDTraj')
#    tmp_item.trajectory = trajectory_from_mdtraj_Trajectory(item, selection=selection,
#                                                            frame_indices=frame_indices,
#                                                            syntaxis=syntaxis)
#    tmp_item.topography = None
#    return tmp_item

def from_pdb(item, topology=None, atom_indices='all', frame_indices='all'):

    from molmodmt import convert
    from .io_trajectory import from_pdb as pdb_to_Trajectory
    from .molmod import MolMod

    if topology is None:
        topology = item

    tmp_item = MolMod()
    tmp_item.topology = convert(topology, to_form='molmodmt.Topology', selection=atom_indices, frame_indices=frame_indices)
    tmp_item.trajectory = pdb_to_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item.topography = None
    tmp_item.structure = None

    return tmp_item

def from_xtc(item, topology=None, atom_indices='all', frame_indices='all'):

    from molmodmt import convert
    from .io_trajectory import from_xtc as xtc_to_Trajectory
    from .molmod import MolMod

    tmp_item = MolMod()
    tmp_item.topology = convert(topology, to_form='molmodmt.Topology', selection=atom_indices, frame_indices=frame_indices)
    tmp_item.trajectory = xtc_to_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item.topography = None
    tmp_item.structure = None

    return tmp_item

def from_hdf5(item, topology=None, atom_indices='all', frame_indices='all'):

    from molmodmt import convert
    from .io_trajectory import from_h5 as h5_to_Trajectory
    from .molmod import MolMod

    if topology is None:
        topology = item

    tmp_item = MolMod()
    tmp_item.topology = convert(topology, to_form='molmodmt.Topology', selection=atom_indices, frame_indices=frame_indices)
    tmp_item.trajectory = h5_to_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item.topography = None
    tmp_item.structure = None

    return tmp_item
