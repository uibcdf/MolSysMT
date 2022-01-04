def to_openmm_Topology(item, selection='all', frame_indices='all', syntaxis='MolSysMT'):

    from molsysmt.tools.molsysmt_Topology import is_molsysmt_Topology
    from molsysmt.basic import convert

    if not is_molsysmt_Topology(item):
        raise ValueError

    tmp_item = convert(item, to_form='openmm.Topology', selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis)

    return tmp_item
