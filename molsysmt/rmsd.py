from ._private_tools.engines import digest_engine
from ._private_tools.frame_indices import digest_frame_indices
from ._private_tools.forms import digest_form
import numpy as _np
from .lib import rmsd as _librmsd

def rmsd (item=None, selection='backbone', frame_indices='all',
          reference_item=None, reference_selection=None, reference_frame_index=0,
          reference_coordinates=None, parallel=True, syntaxis='MolSysMT', engine='MolSysMT'):

    from molsysmt import select, get

    n_atoms, n_frames = get(item, n_atoms=True, n_frames=True)
    atom_indices = select(item, selection=selection, syntaxis=syntaxis)
    n_atom_indices = len(atom_indices)
    frame_indices = _digest_frame_indices(item, frame_indices)
    n_frame_indices = len(frame_indices)
    engine = _digest_engines(engine)

    if engine=='MolSysMT':

        if reference_coordinates is None:

            if reference_item is None:
                reference_item = item

            if reference_selection is None:
                reference_selection = selection

            reference_atom_indices = select(reference_item, selection=reference_selection, syntaxis=syntaxis)

            reference_coordinates = get(reference_item, target='atom', indices=reference_atom_indices,
                                  frame_indices=reference_frame_index, coordinates=True)

        coordinates = get(item, coordinates=True, frame_indices='all')
        length_units = coordinates.unit
        coordinates = _np.asfortranarray(coordinates._value, dtype='float64')
        reference_coordinates = _np.asfortranarray(reference_coordinates._value, dtype='float64')

        if reference_coordinates.shape[1]!=n_atom_indices:
            raise ValueError("reference selection and selection needs to have the same number of atoms")

        rmsd_val = _librmsd.rmsd(coordinates, atom_indices, reference_coordinates, frame_indices,
                                 n_atoms, n_frames, n_atom_indices, n_frame_indices)

        rmsd_val = rmsd_val * length_units
        del(coordinates, length_units)
        return rmsd_val


    elif engine=='MDTraj':
        from mdtraj import rmsd as _mdtraj_rmsd
        rmsd_val = _mdtraj_rmsd(item, ref_item, frame=ref_frame_indices,
                                ref_atom_indices=ref_atom_indices, atom_indices=atom_indices,
                                parallel=parallel, precentered=precentered)
        return rmsd_val

    else:

        raise NotImplementedError

def least_rmsd (item=None, selection='backbone', frame_indices='all',
          reference_item=None, reference_selection=None, reference_frame_index=0,
          reference_coordinates=None, parallel=True, syntaxis='MolSysMT', engine='MolSysMT'):

    from molsysmt import select, get

    n_atoms, n_frames = get(item, n_atoms=True, n_frames=True)
    atom_indices = select(item, selection=selection, syntaxis=syntaxis)
    n_atom_indices = len(atom_indices)
    frame_indices = _digest_frame_indices(item, frame_indices)
    n_frame_indices = len(frame_indices)
    engine = _digest_engines(engine)

    if engine=='MolSysMT':

        if reference_coordinates is None:

            if reference_item is None:
                reference_item = item

            if reference_selection is None:
                reference_selection = selection

            reference_atom_indices = select(reference_item, selection=reference_selection, syntaxis=syntaxis)

            reference_coordinates = get(reference_item, target='atom', indices=reference_atom_indices,
                                  frame_indices=reference_frame_index, coordinates=True)

        coordinates = get(item, coordinates=True, frame_indices='all')
        length_units = coordinates.unit
        coordinates = _np.asfortranarray(coordinates._value, dtype='float64')
        reference_coordinates = _np.asfortranarray(reference_coordinates._value, dtype='float64')

        if reference_coordinates.shape[1]!=n_atom_indices:
            raise ValueError("reference selection and selection needs to have the same number of atoms")

        rmsd_val = _librmsd.least_rmsd(coordinates, atom_indices, reference_coordinates, frame_indices,
                                 n_atoms, n_frames, n_atom_indices, n_frame_indices)

        rmsd_val = rmsd_val * length_units
        del(coordinates, length_units)
        return rmsd_val

    elif engine=='MDTraj':

        raise NotImplementedError

    else:
        raise NotImplementedError

def least_rmsd_fit (item=None, selection='backbone', frame_indices='all',
                    reference_item=None, reference_selection=None, reference_frame_index=0,
                    to_form=None, parallel=True, syntaxis='MolSysMT', engine='MolSysMT'):

    from molsysmt import convert, select, get
    from molsysmt import set as _set

    n_atoms, n_frames = get(item, n_atoms=True, n_frames=True)
    atom_indices = select(item, selection=selection, syntaxis=syntaxis)
    n_atom_indices = len(atom_indices)
    frame_indices = _digest_frame_indices(item, frame_indices)
    n_frame_indices = len(frame_indices)
    engine = _digest_engines(engine)

    if engine=='MolSysMT':

        if reference_item is None:
            reference_item = item

        if reference_selection is None:
            reference_selection = selection

        reference_atom_indices = select(reference_item, selection=reference_selection, syntaxis=syntaxis)

        reference_coordinates = get(reference_item, target='atom', indices=reference_atom_indices,
                                    frame_indices=reference_frame_index, coordinates=True)

        coordinates = get(item, coordinates=True, frame_indices='all')
        length_units = coordinates.unit
        coordinates = _np.asfortranarray(coordinates._value, dtype='float64')
        reference_coordinates = _np.asfortranarray(reference_coordinates._value, dtype='float64')

        if reference_coordinates.shape[1]!=n_atom_indices:
            raise ValueError("reference selection and selection needs to have the same number of atoms")

        _librmsd.least_rmsd_fit(coordinates, atom_indices, reference_coordinates, frame_indices,
                                n_atoms, n_frames, n_atom_indices, n_frame_indices)

        coordinates=_np.ascontiguousarray(coordinates)*length_units

        if to_form is None:

            _set(item, target='system', coordinates=coordinates)
            del(coordinates, length_units)
            pass

        else:

            tmp_item = convert(item, to_form=to_form)
            _set(tmp_item, target='system', coordinates=coordinates)
            del(coordinates, length_units)
            return tmp_item

    elif engine=='MDTraj':

        tmp_item.superpose(tmp_ref_item,frame=ref_frame_indices,atom_indices=atom_indices,ref_atom_indices=ref_atom_indices,parallel=parallel)

        if in_form==x_form:
            item=tmp_item
        elif in_form=='molsysmt.Trajectory':
            item._import_mdtraj_data(tmp_item)
        elif in_form=='molsysmt.MolSys':
            item.trajectory._import_mdtraj_data(tmp_item)
        else:
            item=_convert(tmp_item, to_form=in_form)

    else:

        raise NotImplementedError

def angular_rmsd (item=None, selection='backbone', frame_indices='all',
          reference_item=None, reference_selection=None, reference_frame_index=0,
          reference_coordinates=None, parallel=True, syntaxis='MolSysMT', engine='MolSysMT'):

    raise NotImplementedError

