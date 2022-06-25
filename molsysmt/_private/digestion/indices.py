import numpy as np
from ..exceptions import WrongIndicesError
from ..lists_and_tuples import is_list_or_tuple


def digest_indices(indices):
    """ Checks if indices are of the expected type and value. """
    if isinstance(indices, str):
        if indices.lower() == 'all':
            return 'all'
        else:
            raise WrongIndicesError()
    elif isinstance(indices, (int, np.int64, np.int32)):
        indices = np.array([indices], dtype='int64')
    elif hasattr(indices, '__iter__'):
        indices = np.array(indices, dtype='int64')

    return indices


def digest_atom_indices(atom_indices):
    """ Checks if atom indices are of the expected type and value. """
    return digest_indices(atom_indices)


def digest_group_indices(group_indices):
    """ Checks if group indices are of the expected type and value. """
    return digest_indices(group_indices)


def digest_structure_indices(structure_indices):
    """ Checks if structure indices are of the expected type and value. """
    return digest_indices(structure_indices)


def digest_multiple_structure_indices(structure_indices):
    """ Checks multiple structure indices. """
    if is_list_or_tuple(structure_indices):
        return [digest_structure_indices(ii) for ii in structure_indices]
    else:
        return digest_structure_indices(structure_indices)