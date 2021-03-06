def from_mdanalysis_Universe (item, trajectory_item=None, atom_indices='all', frame_indices='all'):

    from molsysmt.native.molsys import MolSys
    from molsysmt.native.io.topology.classes import from_mdanalysis_Universe as mdanalysis_Universe_to_molsysmt_Topology
    from molsysmt.native.io.trajectory.classes import from_mdanalysis_Universe as mdanalysis_Universe_to_molsysmt_Trajectory

    tmp_item = MolSys()
    tmp_item.topology = mdanalysis_Universe_to_molsysmt_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item.trajectory = mdanalysis_Universe_to_molsysmt_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item

def to_mdanalysis_Universe (item, trajectory_item=None, atom_indices='all', frame_indices='all'):

    raise NotImplementedError
