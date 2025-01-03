import numpy as np

def get_bonded_atom_pairs(group_name, atom_names, atom_indices=None, sorted=True):

    from .get_group_type import get_group_type_from_group_name
    from .amino_acid import get_bonded_atom_pairs as get_bonded_atom_pairs_from_amino_acid
    from .ion import get_bonded_atom_pairs as get_bonded_atom_pairs_from_ion
    from .small_molecule import get_bonded_atom_pairs as get_bonded_atom_pairs_from_small_molecule
    from .terminal_capping import get_bonded_atom_pairs as get_bonded_atom_pairs_from_terminal_capping
    from .water import get_bonded_atom_pairs as get_bonded_atom_pairs_from_water
    from .saccharide import get_bonded_atom_pairs as get_bonded_atom_pairs_from_saccharide

    group_type = get_group_type_from_group_name(group_name)

    bonds = None

    match group_type:

        case 'amino acid':

            bonds = get_bonded_atom_pairs_from_amino_acid(group_name, atom_names, atom_indices=atom_indices,
                                                          sorted=sorted)
        
        case 'ion':

            bonds = get_bonded_atom_pairs_from_ion(group_name, atom_names, atom_indices=atom_indices, sorted=sorted)

        case 'lipid':

            pass

        case 'nucleotide':

            pass

        case 'oligosaccharide':

            pass

        case 'saccharide':

            bonds = get_bonded_atom_pairs_from_saccharide(group_name, atom_names, atom_indices=atom_indices, sorted=sorted)

        case 'small molecule':

            bonds = get_bonded_atom_pairs_from_small_molecule(group_name, atom_names, atom_indices=atom_indices,
                                                              sorted=sorted)

        case 'terminal capping':

            bonds = get_bonded_atom_pairs_from_terminal_capping(group_name, atom_names, atom_indices=atom_indices,
                                                                sorted=sorted)

        case 'water':

            bonds = get_bonded_atom_pairs_from_water(atom_names, atom_indices=atom_indices, sorted=sorted)


        case _:
            print(f'Warning! The amino acid {group_name} has no template.')

    return bonds

