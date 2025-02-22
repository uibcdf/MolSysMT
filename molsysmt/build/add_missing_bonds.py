from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest
from molsysmt._private.variables import is_all

@digest()
def add_missing_bonds(molecular_system, max_bond_length='2 angstroms', selection='all',
                      structure_index=0, syntax='MolSysMT', engine='MolSysMT',
                      in_place=True, skip_digestion=False):
    """
    To be written soon...
    """

    if engine=='MolSysMT':

        from molsysmt.build import get_missing_bonds
        from molsysmt.build import add_bonds

        bonds = get_missing_bonds(molecular_system, max_bond_length=max_bond_length, selection=selection,
                                 structure_index=structure_index, syntax=syntax,
                                 skip_digestion=True)
        return add_bonds(molecular_system, bonds, in_place=in_place, skip_digestion=True)

    else:

        raise NotImplementedError

