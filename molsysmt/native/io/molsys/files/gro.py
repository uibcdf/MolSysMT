def from_gro(item, trajectory_item=None, atom_indices='all', frame_indices='all'):

    from molsysmt.native import MolSys
    from molsysmt.native.io.topology.files import from_gro as gro_to_molsysmt_Topology
    from molsysmt import convert

    if trajectory_item is None:
        trajectory_item = item

    tmp_item = MolSys()
    tmp_item.topology = gro_to_molsysmt_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item.trajectory = convert(trajectory_item, to_form='molsysmt.Trajectory', selection=atom_indices, frame_indices=frame_indices)

    return tmp_item

