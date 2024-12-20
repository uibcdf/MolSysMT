from molsysmt._private.variables import is_all
from molsysmt.element import is_composed_of, is_element
from molsysmt.element import _plural_elements_to_singular, _singular_element_to_plural
from molsysmt.element.group import _plural_group_types_to_singular
from molsysmt.element.group import is_group_type
from molsysmt.element.molecule import _plural_molecule_types_to_singular
from molsysmt.element.molecule import is_molecule_type
import numpy as np
import pandas as pd
from networkx import Graph
from importlib import import_module

def _auxiliary_getter(function, item, indices='all'):

    module = import_module(function.__module__)
    function_name = function.__name__

    words = function_name.split('_')

    if function_name == 'get_bond_index_from_atom':

        return _get_bond_index_from_atom(module, item, indices)

    elif function_name == 'get_bonded_atoms_from_atom':

        return _get_bonded_atoms_from_atom(module, item, indices)

    elif function_name == 'get_bonded_atoms_pairs_from_atom':

        return _get_bonded_atoms_pairs_from_atom(module, item, indices)

    elif function_name == 'get_inner_bond_index_from_atom':

        return _get_inner_bond_index_from_atom(module, item, indices)

    elif function_name == 'get_inner_bonded_atoms_from_atom':

        return _get_inner_bonded_atoms_from_atom(module, item, indices)

    elif function_name == 'get_inner_bonded_atoms_pairs_from_atom':

        return _get_inner_bonded_atoms_pairs_from_atom(module, item, indices)

    elif function_name == 'get_n_bonds_from_atom':

        return _get_n_bonds_from_atom(module, item, indices)

    elif function_name == 'get_n_inner_bonds_from_atom':

        return _get_n_inner_bonds_from_atom(module, item, indices)

    elif function_name == 'get_bonded_atoms_from_system':

        return _get_bonded_atoms_from_atom(module, item, 'all')

    elif function_name == 'get_bonded_atoms_pairs_from_system':

        return _get_bonded_atoms_pairs_from_atom(module, item, 'all')

    elif function_name == 'get_inner_bonded_atoms_from_system':

        return _get_bonded_atoms_from_atom(module, item, 'all')

    elif function_name == 'get_inner_bonded_atoms_pairs_from_system':

        return _get_bonded_atoms_from_atom(module, item, 'all')

    elif function_name == 'get_bonded_atoms_pairs_from_bond':

        return _get_bonded_atoms_pairs_from_bond(module, item, indices)

    elif 'n' == words[1]:

        aux_word = function_name.split('get_n_')[-1].split('_from_')[0].replace('_', ' ')

        if is_element(aux_word):

            involved_element = _plural_elements_to_singular[words[2]]
            base_element = words[-1]

            if involved_element == base_element:

                return _get_n_elements(module, base_element, item, indices)

            else:

                if is_composed_of(base_element, involved_element):

                    return _get_n_inf_from_element(module, involved_element, base_element, item, indices)

                else:

                    return _get_n_sup_from_element(module, involved_element, base_element, item, indices)

        elif is_group_type(aux_word):

            base_element = words[-1]
            if aux_word in _plural_group_types_to_singular:
                aux_word = _plural_group_types_to_singular[aux_word]

            if base_element == 'system':

                return _get_n_group_type_from_system(module, aux_word, item)

            else:

                return _get_n_group_type_from_element(module, aux_word, base_element, item, indices)

        elif is_molecule_type(aux_word):

            base_element = words[-1]
            if aux_word in _plural_molecule_types_to_singular:
                aux_word = _plural_molecule_types_to_singular[aux_word]

            if base_element == 'system':

                return _get_n_molecule_type_from_system(module, aux_word, item)

            else:

                return _get_n_molecule_type_from_element(module, aux_word, base_element, item, indices)

        else:

            raise NotImplementedError

    elif 'index' == words[2]:

        involved_element = words[1]
        base_element = words[-1]

        if involved_element == base_element:

            return _get_index_from_element(module, base_element, item, indices)

        else:

            if is_composed_of(base_element, involved_element):

                return _get_inf_index_from_element(module, involved_element, base_element, item, indices)

            else:

                return _get_sup_index_from_element(module, involved_element, base_element, item, indices)

    elif is_element(words[1]):

        involved_element = words[1]
        attribute = words[2]
        base_element = words[-1]

        if involved_element == base_element:

            raise NotImplementedError

        else:

            if is_composed_of(base_element, involved_element):

                return _get_inf_attr_from_element(module, involved_element, attribute, base_element, item,
                                                  indices)

            else:

                return _get_sup_attr_from_element(module, involved_element, attribute, base_element, item,
                                                  indices)
    else:

        raise NotImplementedError


# n elements


def _get_n_elements(module, element, item, indices):

    if is_all(indices):
        aux_get = getattr(module, f'get_n_{_singular_element_to_plural[element]}_from_system')
        output = aux_get(item)
    else:
        output = indices.shape[0]

    return output


def _get_n_inf_from_element(module, involved_element, base_element, item, indices):

    aux_get = getattr(module, f'get_{involved_element}_index_from_{base_element}')
    output = aux_get(item, indices)
    output = [len(ii) for ii in output]

    return output


def _get_n_sup_from_element(module, involved_element, base_element, item, indices):

    if is_all(indices):
        aux_get = getattr(module, f'get_n_{_singular_element_to_plural[involved_element]}_from_system')
        output = aux_get(item)
    else:
        aux_get = getattr(module, f'get_{involved_element}_index_from_{base_element}')
        output = aux_get(item, indices=indices)
        output = np.unique(output).shape[0]

    return output


# n index

def _get_index_from_element(module, element, item, indices):

    if is_all(indices):
        aux_get = getattr(module, f'get_n_{_singular_element_to_plural[element]}_from_system')
        n_aux = aux_get(item)
        output = np.arange(n_aux, dtype=int).tolist()
    else:
        output = indices.tolist()

    return output


def _get_inf_index_from_element(module, involved_element, base_element, item, indices):

    from molsysmt.config import large_list_length

    aux_get = getattr(module, f'get_{base_element}_index_from_{involved_element}')
    target_index = aux_get(item)

    if len(target_index) > large_list_length:

        serie = pd.Series(target_index)
        groups_serie = serie.groupby(serie).apply(lambda x: x.index.tolist())
        if is_all(indices):
            output = [ii for ii in groups_serie]
        else:
            output = [groups_serie[ii] for ii in indices]

    else:

        indice_dict = {}

        for idx, num in enumerate(target_index):
            try:
                indice_dict[num].append(idx)
            except KeyError:
                indice_dict[num] = [idx]

        if is_all(indices):
            output = [indice_dict[ii] for ii in indice_dict.keys()]
        else:
            output = [indice_dict[ii] for ii in indices]

    return output


def _get_sup_index_from_element(module, involved_element, base_element, item, indices):

    get_1 = getattr(module, f'get_atom_index_from_{base_element}')
    get_2 = getattr(module, f'get_{involved_element}_index_from_atom')

    atom_index_from_target = get_1(item, indices=indices)
    first_atom_index_from_target = np.array([ii[0] for ii in atom_index_from_target])
    output = get_2(item, indices=first_atom_index_from_target)

    del atom_index_from_target, first_atom_index_from_target

    return output


# attrs


def _get_inf_attr_from_element(module, involved_element, attribute, base_element, item, indices):

    get_1 = getattr(module, f'get_{involved_element}_index_from_{base_element}')
    target_indices = get_1(item, indices=indices)
    get_2 = getattr(module, f'get_{involved_element}_{attribute}_from_{involved_element}')

    aux_unique_indices, aux_indices = np.unique(np.concatenate(target_indices), return_inverse=True)
    aux_vals = get_2(item, indices=aux_unique_indices)
    aux_output = np.array(aux_vals)[aux_indices]
    output = []
    ii = 0
    for aux in target_indices:
        jj = ii+len(aux)
        output.append(aux_output[ii:jj].tolist())
        ii = jj

    del aux_unique_indices, aux_vals, aux_output, target_indices

    return output


def _get_sup_attr_from_element(module, involved_element, attribute, base_element, item, indices):

    get_1 = getattr(module, f'get_{involved_element}_index_from_{base_element}')
    get_2 = getattr(module, f'get_{involved_element}_{attribute}_from_{involved_element}')

    aux_indices = get_1(item, indices=indices)
    aux_unique_indices, aux_new_indices = np.unique(aux_indices, return_inverse=True)
    aux_vals = get_2(item, indices=aux_unique_indices)
    output = np.array(aux_vals)[aux_new_indices]

    del aux_indices, aux_unique_indices, aux_vals, aux_new_indices

    return output.tolist()


# n group or molecule types


def _get_n_group_type_from_element(module, group_type, element, item, indices):

    get_1 = getattr(module, f'get_group_index_from_{element}')
    get_2 = getattr(module, 'get_group_type_from_group')

    group_indices = get_1(item, indices=indices)
    if element in ['component', 'molecule', 'entity', 'chain']:
        group_indices=np.concatenate([np.array(ii) for ii in group_indices])
    group_indices = np.unique(group_indices)
    group_types = get_2(item, indices=group_indices)
    output = (np.array(group_types) == group_type).sum()

    return output


def _get_n_group_type_from_system(module, group_type, item):

    get_1 = getattr(module, 'get_group_type_from_group')

    group_types = get_1(item)
    output = (np.array(group_types) == group_type).sum()

    return output


def _get_n_molecule_type_from_element(module, molecule_type, element, item, indices):

    get_1 = getattr(module, f'get_molecule_index_from_{element}')
    get_2 = getattr(module, 'get_molecule_type_from_molecule')

    molecule_indices = get_1(item, indices=indices)
    molecule_indices = np.unique(molecule_indices)
    molecule_types = get_2(item, indices=molecule_indices)
    output = (np.array(molecule_types) == molecule_type).sum()

    return output


def _get_n_molecule_type_from_system(module, molecule_type, item):

    get_1 = getattr(module, 'get_molecule_type_from_molecule')

    molecule_types = get_1(item)
    output = (np.array(molecule_types) == molecule_type).sum()

    return output


# bonds

def _get_bond_index_from_atom(module, item, indices):

    aux_get = getattr(module, 'get_bonded_atoms_pairs_from_bond')

    output = None

    G = Graph()
    edges = aux_get(item)
    n_bonds = len(edges)
    edge_indices = np.array([{'index': ii} for ii in range(n_bonds)]).reshape([n_bonds, 1])
    G.add_edges_from(np.hstack([edges, edge_indices]))

    if is_all(indices):

        aux_get = getattr(module, 'get_atom_index_from_atom')
        indices = aux_get(item)

    output = []

    for ii in indices:
        if ii in G:
            output.append([n['index'] for n in G[ii].values()])
        else:
            output.append([])

    del G, edges, edge_indices

    return output


def _get_bonded_atoms_from_atom(module, item, indices):

    output = None

    aux_get_1 = getattr(module, 'get_bonded_atoms_pairs_from_bond')
    aux_get_2 = getattr(module, 'get_atom_index_from_atom')

    G = Graph()
    edges = aux_get_1(item)
    
    G.add_edges_from(edges)

    if is_all(indices):

        indices = aux_get_2(item)

    output = []

    for ii in indices:
        if ii in G:
            output.append(list(G.neighbors(ii)))
        else:
            output.append([])

    del G, edges

    return output


def _get_bonded_atoms_pairs_from_atom(module, item, indices):

    output = None

    aux_get_1 = getattr(module, 'get_bonded_atoms_pairs_from_bond')

    if is_all(indices):

        output = aux_get_1(item)
   
    else:

        pairs = aux_get_1(item)
        pairs = np.array(pairs)
        mask = np.isin(pairs[:,0], indices) | np.isin(pairs[:,1], indices)
        output = pairs[mask,:].tolist()

        del pairs, mask

    return output


def _get_inner_bond_index_from_atom(module, item, indices):

    aux_get = getattr(module, 'get_bonded_atoms_pairs_from_bond')

    output = None

    G = Graph()
    edges = aux_get(item)
    n_bonds = len(edges)
    edge_indices = np.array([{'index': ii} for ii in range(n_bonds)]).reshape([n_bonds, 1])
    G.add_edges_from(np.hstack([edges, edge_indices]))

    if is_all(indices):

        aux_get = getattr(module, 'get_atom_index_from_atom')
        indices = aux_get(item)

    else:

        G = G.subgraph(indices)

    output = []

    for ii in indices:
        if ii in G:
            output.append([n['index'] for n in G[ii].values()])
        else:
            output.append([])

    del G, edges, edge_indices

    return output

def _get_inner_bonded_atoms_from_atom(module, item, indices):

    output = None

    aux_get_1 = getattr(module, 'get_bonded_atoms_pairs_from_bond')

    G = Graph()
    edges = aux_get_1(item)
    
    G.add_edges_from(edges)

    if not is_all(indices):

        G = G.subgraph(indices)

    output = []
    for nodo in G.nodes():
        output.append(list(G.neighbors(nodo)))

    del G, edges

    return output


def _get_inner_bonded_atoms_pairs_from_atom(module, item, indices):

    output = None

    aux_get_1 = getattr(module, 'get_bonded_atoms_pairs_from_bond')

    if is_all(indices):

        output = aux_get_1(item)
   
    else:

        pairs = aux_get_1(item)
        pairs = np.array(pairs)
        mask = np.isin(pairs[:,0], indices) * np.isin(pairs[:,1], indices)
        output = pairs[mask,:].tolist()

        del pairs, mask

    return output


def _get_n_bonds_from_atom(module, item, indices):

    if is_all(indices):

        aux_get = getattr(module, 'get_n_bonds_from_system')
        output = aux_get(item)

    else:

        aux_get = getattr(module, 'get_bond_index_from_atom')
        bond_indices = aux_get(item, indices)
        output = np.unique(np.concatenate(bond_indices)).shape[0]
        del bond_indices

    return output


def _get_n_inner_bonds_from_atom(module, item, indices):

    if is_all(indices):

        aux_get = getattr(module, 'get_n_bonds_from_system')
        output = aux_get(item)

    else:

        aux_get = getattr(module, 'get_inner_bond_index_from_atom')
        bond_indices = aux_get(item, indices)
        output = np.unique(np.concatenate(bond_indices)).shape[0]
        del bond_indices

    return output


def _get_bonded_atoms_pairs_from_bond(module, item, indices):

    aux_get = getattr(module, 'get_bonded_atoms_from_bond')

    output = aux_get(item, indices)

    return output

