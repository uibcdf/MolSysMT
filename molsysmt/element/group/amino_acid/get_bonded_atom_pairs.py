from molsysmt._private.digestion import digest
import numpy as np

_sorted=sorted

@digest()
def get_bonded_atom_pairs(group_name, atom_names, atom_indices=None, sorted=True, skip_digestion=False):

    from molsysmt.element.group.amino_acid import group_names, get_group_db

    if group_name not in group_names:
        return None
    
    if atom_indices is None:
        atom_indices = np.arange(len(atom_names), dtype=int).tolist()

    aux_group_names = [group_name]

    if 'C'+group_name in group_names:
        aux_group_names.append('C'+group_name)

    if 'N'+group_name in group_names:
        aux_group_names.append('N'+group_name)

    aux_dict = {}
    for ii,jj in zip(atom_names, atom_indices):
        if ii not in aux_dict:
            aux_dict[ii]=[jj]
        else:
            aux_dict[ii].append(jj)

    for aux_group_name in aux_group_names:

        db = get_group_db(aux_group_name)
        
        is_in = -1
        for ii,jj in enumerate(db['topology']):
            if np.all(np.isin(atom_names, jj['atoms'])):
                is_in=ii
                break

        if is_in!=-1:

            bonds = []
            for ii,jj in db['topology'][is_in]['bonds']:
                if ii in atom_names:
                    if jj in atom_names:
                        for iii in aux_dict[ii]:
                            for jjj in aux_dict[jj]:
                                if iii<jjj:
                                    bonds.append([iii,jjj])
                                else:
                                    bonds.append([jjj,iii])
            if sorted:
                return _sorted(bonds)
            else:
                return bonds


    if group_name in ['HIS']:
        for aux_group_name in group_names:
            try:

                db = get_group_db(aux_group_name)
                for ii,jj in enumerate(db['topology']):
                    if len(atom_names)==len(jj['atoms']):
                        if np.all(np.isin(atom_names, jj['atoms'])):
                            if np.all(np.isin(jj['atoms'], atom_names)):
 
                                bonds = []
                                for aa,bb in jj['bonds']:
                                    if aa in atom_names:
                                        if bb in atom_names:
                                            iii = atom_indices[atom_names.index(aa)]
                                            jjj = atom_indices[atom_names.index(bb)]
                                            if iii<jjj:
                                                bonds.append([iii,jjj])
                                            else:
                                                bonds.append([jjj,iii])
                                if sorted:
                                    return _sorted(bonds)
                                else:
                                    return bonds

            except:
                pass

    print(f'Warning! The amino acid {group_name} has no template.')
    print(f'No bonds were added by element.group.amino_acid.get_bonded_atom_pairs')

    return None

