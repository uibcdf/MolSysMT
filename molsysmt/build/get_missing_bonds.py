from molsysmt._private.digestion import digest
from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.variables import is_all
import numpy as np
import warnings

_sorted=sorted

# Protein:
# Enlace C-N: aproximadamente 1.33 Å
# Enlace C-C: aproximadamente 1.54 Å
# Enlace C-S: aproximadamente 1.82 Å
# Small molecule:
# Enlace C-H: aproximadamente 1.09 Å
# Enlace C-C: aproximadamente 1.54 Å
# Enlace C-O: aproximadamente 1.43 Å
# Enlace C-N: aproximadamente 1.47 Å
# Water molecule:
# Enlace O-H: aproximadamente 0.96 Å
# Lipid:
# Enlace C-H: aproximadamente 1.09 Å
# Enlace C-C: aproximadamente 1.54 Å
# Enlace P-O: aproximadamente 1.61 Å


@digest()
def get_missing_bonds(molecular_system, threshold='2 angstroms', selection='all',
                      structure_index=0, syntax='MolSysMT', engine='MolSysMT',
                      sorted=True, with_templates=True, skip_digestion=False):
    """
    To be written soon...
    """

    bonds = []

    if engine=="MolSysMT":

        from molsysmt import select, get
        from molsysmt.structure import get_contacts
        from molsysmt.element.group.water import get_bonded_atom_pairs as _bonds_in_water
        from molsysmt.element.group.ion import get_bonded_atom_pairs as _bonds_in_ion
        from molsysmt.element.group.amino_acid import get_bonded_atom_pairs as _bonds_in_amino_acid
        from molsysmt.element.group.terminal_capping import get_bonded_atom_pairs as _bonds_in_terminal_capping
        from molsysmt.element.group.small_molecule import get_bonded_atom_pairs as _bonds_in_small_molecule
        from molsysmt.element.group.saccharide import get_bonded_atom_pairs as _bonds_in_saccharide
        from molsysmt.element.group.terminal_capping import is_n_terminal_capping, is_c_terminal_capping

        old_bonds = get(molecular_system, selection=selection, inner_bonded_atom_pairs=True)

        if with_templates:

            aux_lists = get(molecular_system, element='group', selection=selection, group_name=True,
                            group_type=True, atom_index=True, atom_name=True,
                            skip_digestion=True)

            group_index = -1
            groups_undone = []
            atoms_undone = []

            aux_peptidic_bonds_C={}
            aux_peptidic_bonds_N={}

            bonds = []

            for group_name, group_type, atom_indices, atom_names in zip(*aux_lists):

                group_index += 1

                if group_type=="water": # Use match-case whenever Python 3.9 is deprecated

                    aux_bonds = _bonds_in_water(atom_names, atom_indices, sorted=False)
                    bonds += aux_bonds

                elif group_type=="ion":
                        
                    aux_bonds = _bonds_in_ion(group_name, atom_names, atom_indices, sorted=False)
                    if aux_bonds is None:
                        aux_bonds = _bonds_in_unknown_group(molecular_system, atom_indices, atom_names,
                                                            structure_index=structure_index, threshold=threshold,
                                                            sorted=False)
                    bonds += aux_bonds

                elif group_type=='amino acid':

                    aux_bonds = _bonds_in_amino_acid(group_name, atom_names, atom_indices, sorted=False)
                    if aux_bonds is None:
                        aux_bonds = _bonds_in_unknown_group(molecular_system, atom_indices, atom_names,
                                                            structure_index=structure_index, threshold=threshold,
                                                            sorted=False)
                    bonds += aux_bonds
                    
                    if 'C' in atom_names:
                        aux_peptidic_bonds_C[group_index]=atom_indices[atom_names.index('C')]

                    if 'N' in atom_names:
                        aux_peptidic_bonds_N[group_index]=atom_indices[atom_names.index('N')]

                elif group_type=='terminal capping':

                    aux_bonds = _bonds_in_terminal_capping(group_name, atom_names, atom_indices, sorted=False)
                    if aux_bonds is None:
                        aux_bonds = _bonds_in_unknown_group(molecular_system, atom_indices, atom_names,
                                                            structure_index=structure_index, threshold=threshold,
                                                            sorted=False)
                    bonds += aux_bonds

                    if is_c_terminal_capping(group_name):
                        aux_peptidic_bonds_C[group_index]=atom_indices[atom_names.index('C')]
                    elif is_n_terminal_capping(group_name):
                        aux_peptidic_bonds_N[group_index]=atom_indices[atom_names.index('N')]
                    else:
                        raise ValueError("terminal capping not recognized as C- or N-")

                elif group_type=='small molecule':

                    aux_bonds = _bonds_in_small_molecule(group_name, atom_names, atom_indices, sorted=False)
                    if aux_bonds is None:
                        aux_bonds = _bonds_in_unknown_group(molecular_system, atom_indices, atom_names,
                                                            structure_index=structure_index, threshold=threshold,
                                                            sorted=False)
                    bonds += aux_bonds

                elif group_type=='saccharide':

                    aux_bonds = _bonds_in_saccharide(group_name, atom_names, atom_indices, sorted=False)
                    if aux_bonds is None:
                        aux_bonds = _bonds_in_unknown_group(molecular_system, atom_indices, atom_names,
                                                            structure_index=structure_index, threshold=threshold,
                                                            sorted=False)
                    bonds += aux_bonds

                elif group_type=='oligosaccharide':

                    raise NotImplementedError('Group type "oligosaccharide" not implemented')

                elif group_type=='lipid':

                    raise NotImplementedError('Group type "lipid" not implemented')

                elif group_type=='nucleotide':

                    raise NotImplementedError('Group type "nucleotide" not implemented')

                else:

                    groups_undone.append(group_index)

            # peptidic bonds

            aux_C = []
            aux_N = []

            for group_index in aux_peptidic_bonds_C.keys():
                if group_index+1 in aux_peptidic_bonds_N:
                    aux_C.append(aux_peptidic_bonds_C[group_index])
                    aux_N.append(aux_peptidic_bonds_N[group_index+1])

            if len(aux_C):
                peptidic_bonds = get_contacts(molecular_system, selection=aux_C, selection_2=aux_N,
                                              threshold=threshold, pairs=True, output_type='pairs',
                                              output_indices='atom', pbc=True, skip_digestion=True)[0]

                bonds += peptidic_bonds

            del(aux_lists, group_name, group_type, atom_indices, atom_names)
            del(aux_peptidic_bonds_C, aux_peptidic_bonds_N, aux_C, aux_N)
            
            if len(groups_undone):
                raise NotImplementedError('Some groups not defined with templates')
            if len(atoms_undone):
                raise NotImplementedError('Some atoms not defined with templates')

            if not is_all(selection):
                mask =  select(molecular_system, element='atom', selection=selection)
                tmp_bonds = []
                for bond in bonds:
                    if (bond[0] in mask) and (bond[1] in mask):
                        tmp_bonds += bond
                bonds = tmp_bonds

        else:

            atom_indices, atom_names, atom_types, group_indices, group_types = get(molecular_system, element='atom',
                                                                               selection=selection,
                                                                               atom_index=True, atom_name=True,
                                                                               atom_type=True, group_index=True,
                                                                               group_type=True, skip_digestion=True)

            heavy_atoms=[]
            heavy_atoms_name=[]
            heavy_atoms_group_index=[]
            heavy_atoms_group_type=[]
            h_atoms=[]
            h_atoms_group_index=[]

            for index, atom_name, atom_type, group_index, group_type in zip(atom_indices, atom_names, atom_types,
                                                                            group_indices, group_types):
                if 'H'==atom_type:
                    h_atoms.append(index)
                    h_atoms_group_index.append(group_index)
                else:
                    heavy_atoms.append(index)
                    heavy_atoms_name.append(atom_name)
                    heavy_atoms_group_index.append(group_index)
                    heavy_atoms_group_type.append(group_type)

            heavy_bonds = get_contacts(molecular_system, selection=heavy_atoms,
                                       structure_indices = structure_index, threshold=threshold,
                                       output_type='pairs', output_indices='selection', pbc=True,
                                       skip_digestion=True)[0]

            h_bonds = get_contacts(molecular_system, selection=heavy_atoms, selection_2=h_atoms,
                                   structure_indices = structure_index, threshold=threshold,
                                   output_type='pairs', output_indices='selection', pbc=True, skip_digestion=True)[0]

            bonds_with_distance = []

            for pair in heavy_bonds:
                ii,jj=pair
                if heavy_atoms_group_index[ii]==heavy_atoms_group_index[jj]:
                    if heavy_atoms_group_type[ii]=='amino acid':
                        ii_name = heavy_atoms_name[ii]
                        jj_name = heavy_atoms_name[jj]
                        if 'N' in [ii_name, jj_name]:
                            if set(['N','CA'])==set([ii_name, jj_name]):
                                ii = heavy_atoms[ii]
                                jj = heavy_atoms[jj]
                                if ii<jj:
                                    bonds_with_distance.append([ii,jj])
                                else:
                                    bonds_with_distance.append([jj,ii])
                        elif 'C' in [ii_name, jj_name]:
                            if set(['C','CA'])==set([ii_name, jj_name]):
                                ii = heavy_atoms[ii]
                                jj = heavy_atoms[jj]
                                if ii<jj:
                                    bonds_with_distance.append([ii,jj])
                                else:
                                    bonds_with_distance.append([jj,ii])
                            elif set(['C','O'])==set([ii_name, jj_name]):
                                ii = heavy_atoms[ii]
                                jj = heavy_atoms[jj]
                                if ii<jj:
                                    bonds_with_distance.append([ii,jj])
                                else:
                                    bonds_with_distance.append([jj,ii])
                        elif 'CA' in [ii_name, jj_name]:
                            if set(['CA','CB'])==set([ii_name, jj_name]):
                                ii = heavy_atoms[ii]
                                jj = heavy_atoms[jj]
                                if ii<jj:
                                    bonds_with_distance.append([ii,jj])
                                else:
                                    bonds_with_distance.append([jj,ii])
                        else:
                            ii = heavy_atoms[ii]
                            jj = heavy_atoms[jj]
                            if ii<jj:
                                bonds_with_distance.append([ii,jj])
                            else:
                                bonds_with_distance.append([jj,ii])
                    else:
                        ii = heavy_atoms[ii]
                        jj = heavy_atoms[jj]
                        if ii<jj:
                            bonds_with_distance.append([ii,jj])
                        else:
                            bonds_with_distance.append([jj,ii])
                elif heavy_atoms_name[ii]=='C' and heavy_atoms_name[jj]=='N':
                    if heavy_atoms_group_type[ii] in ['amino acid', 'terminal capping'] and heavy_atoms_group_type[jj] in ['amino acid', 'terminal capping']:
                        if heavy_atoms_group_index[ii]+1==heavy_atoms_group_index[jj]:
                            ii = heavy_atoms[ii]
                            jj = heavy_atoms[jj]
                            if ii<jj:
                                bonds_with_distance.append([ii,jj])
                            else:
                                bonds_with_distance.append([jj,ii])
                elif heavy_atoms_name[ii]=='N' and heavy_atoms_name[jj]=='C':
                    if heavy_atoms_group_type[ii] in ['amino acid', 'terminal capping'] and heavy_atoms_group_type[jj] in ['amino acid', 'terminal capping']:
                        if heavy_atoms_group_index[ii]==heavy_atoms_group_index[jj]+1:
                            ii = heavy_atoms[ii]
                            jj = heavy_atoms[jj]
                            if ii<jj:
                                bonds_with_distance.append([ii,jj])
                            else:
                                bonds_with_distance.append([jj,ii])

            for pair in h_bonds:
                ii,jj=pair
                if heavy_atoms_group_index[ii]==h_atoms_group_index[jj]:
                    if heavy_atoms_group_type[ii]=='amino acid':
                        if heavy_atoms_name[ii] not in ['CA','C','O']:
                            ii = heavy_atoms[ii]
                            jj = h_atoms[jj]
                            if ii<jj:
                                bonds_with_distance.append([ii,jj])
                            else:
                                bonds_with_distance.append([jj,ii])
                    else:
                        ii = heavy_atoms[ii]
                        jj = h_atoms[jj]
                        if ii<jj:
                            bonds_with_distance.append([ii,jj])
                        else:
                            bonds_with_distance.append([jj,ii])

            bonds += bonds_with_distance

        if old_bonds:

            tmp_bonds = []
            for ii in bonds:
                if ii not in old_bonds:
                    tmp_bonds.append(ii)
            bonds = tmp_bonds

    elif engine=="pytraj":

        from molsysmt.basic import convert, get
        from os import remove
        from molsysmt._private.files_and_directories import temp_filename

        old_bonds = get(molecular_system, element='atom', selection=atom_indices, inner_bonded_atoms=True)

        for ii in range(old_bonds):
            if old_bonds[ii][0]>old_bonds[ii][1]:
                old_bonds[ii][0], old_bonds[ii][1] = old_bonds[ii][1], old_bonds[ii][0]


        temp_pdb_file = temp_filename(extension='pdb')
        temp_molecular_system = convert(molecular_system, to_form=temp_pdb_file)
        temp_molecular_system = convert(temp_molecular_system, to_form="pytraj.Topology", threshold=threshold)

        new_bonds = get(molecular_system, element='atom', selection=atom_indices, inner_bonded_atoms=True)

        for ii in range(old_bonds):
            if old_bonds[ii][0]>old_bonds[ii][1]:
                old_bonds[ii][0], old_bonds[ii][1] = old_bonds[ii][1], old_bonds[ii][0]

        for bond in new_bonds:
            if bond not in old_bonds:
                output.append(bond)

        bonds = output

    else:

        raise NotImplementedMethodError

    if sorted:
        bonds = _sorted(bonds)

    return bonds

def _bonds_in_unknown_group(molecular_system, atom_indices, atom_names, structure_index=0,
                            threshold='2 angstroms', sorted=False):

    from molsysmt.element.atom import get_atom_type_from_atom_name
    from molsysmt.structure import get_contacts

    heavy_atoms=[]
    h_atoms=[]

    for index, name in zip(atom_indices, atom_names):
        if 'H'==get_atom_type_from_atom_name(name):
            h_atoms.append(index)
        else:
            heavy_atoms.append(index)

    heavy_bonds = get_contacts(molecular_system, selection=heavy_atoms,
                               structure_indices = structure_index, threshold=threshold,
                               output_type='pairs', output_indices='atom', pbc=True, skip_digestion=True)[0]

    h_bonds = get_contacts(molecular_system, selection=heavy_atoms, selection_2=h_atoms,
                           structure_indices = structure_index, threshold=threshold,
                           output_type='pairs', output_indices='atom', pbc=True, skip_digestion=True)[0]

    bonds = heavy_bonds + h_bonds

    if sorted:
        bonds = _sorted(bonds)

    return bonds

