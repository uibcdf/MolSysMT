from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def to_XYZ(item, atom_indices='all', structure_indices='all', check=True):

    if check:

        digest_item(item, 'molsysmt.Structures')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    from . import get_coordinates_from_atom
    tmp_item = get_coordinates_from_atom(item, indices=atom_indices, structure_indices=structure_indices, check=False)

    return tmp_item
