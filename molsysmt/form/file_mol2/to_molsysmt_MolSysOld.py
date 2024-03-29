from molsysmt._private.digestion import digest

@digest(form='file:mol2')
def to_molsysmt_MolSysOld(item, atom_indices='all', structure_indices='all', skip_digestion=False):

    from molsysmt.native import MolSysOld
    from . import to_molsysmt_TopologyOld
    from . import to_molsysmt_StructuresOld

    tmp_item = MolSysold()
    tmp_item.topology = to_molsysmt_TopologyOld(item, atom_indices=atom_indices)
    tmp_item.trajectory = to_molsysmt_StructuresOld(item, atom_indices=atom_indices,
                                                    structure_indices=structure_indices,
                                                    skip_digestion=True)

    return tmp_item
