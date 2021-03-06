from ._private_tools.engines import digest_engine
from ._private_tools.frame_indices import digest_frame_indices
from ._private_tools.forms import digest_form
from molsysmt.lib import box as _libbox
import numpy as np
import pyunitwizard as puw
from molsysmt import __quantities_form__

def box_shape_from_box_angles(angles):

    import numpy as np

    shape = None

    alpha = angles[:,0].mean()
    beta = angles[:,1].mean()
    gamma = angles[:,2].mean()

    alpha = np.round(alpha, 2)
    beta = np.round(beta, 2)
    gamma = np.round(gamma, 2)

    if alpha==90.00 and beta==90.00 and gamma==90.00:
        shape = 'cubic'
    else:
        shape = 'triclinic'

    return shape

def box_shape_from_box_vectors(box):

    from molsysmt.lib import box as _libbox
    
    if box == None:
        return None

    else:
        
        n_frames = box.shape[0]
        angles = _libbox.angles_box(box._value, n_frames)
        return box_shape_from_box_angles(angles)

def box_lengths_from_box_vectors(box):

    tmp_length_unit_name = puw.get_unit_name(box)
    n_frames = box.shape[0]
    tmp_box =  np.asfortranarray(puw.get_value(box), dtype='float64')
    lengths = _libbox.length_edges_box(tmp_box, n_frames)
    lengths = np.ascontiguousarray(lengths, dtype='float64')
    del(tmp_box)

    return puw.quantity(lengths.round(6), tmp_length_unit_name, __quantities_form__)

def box_angles_from_box_vectors(box):

    from molsysmt._private_tools.units import angle_unit_name

    n_frames = box.shape[0]
    tmp_box =  np.asfortranarray(puw.get_value(box), dtype='float64')
    angles = _libbox.angles_box(tmp_box, n_frames)
    angles = np.ascontiguousarray(angles, dtype='float64')
    del(tmp_box)

    return puw.quantity(angles.round(6), angle_unit_name, __quantities_form__)

def box_vectors_from_box_lengths_and_angles(lengths, angles):


    tmp_length_unit_name = puw.get_unit_name(lengths)
    lengths_value = puw.get_value(lengths)
    angles_unit_name = puw.get_unit_name(angles)
    angles_value = puw.get_value(angles)
    tmp_lengths =  np.asfortranarray(lengths_value, dtype='float64')
    tmp_angles =  np.asfortranarray(angles_value, dtype='float64')
    n_frames = lengths.shape[0]

    box = _libbox.lengths_and_angles_to_box(tmp_lengths, tmp_angles, n_frames)
    box = np.ascontiguousarray(box, dtype='float64')

    del(tmp_lengths, tmp_angles)

    return puw.quantity(box.round(6), tmp_length_unit_name, __quantities_form__)

def box_volume_from_box_vectors(box):

    n_frames = box.shape[0]
    tmp_length_unit_name = puw.get_unit_name(box)

    if box[0] is None:
        return np.full(n_frames, None)*puw.unit(tmp_length_unit_name, __quantities_form__)**3
    else:
        output = np.empty(n_frames, dtype=float)*puw.unit(tmp_length_unit, __quantities_form__)**3
        for ii in range(n_frames):
            aux = np.cross(box[ii,1,:], box[ii,2,:])
            aux2 = np.dot(box[ii,0,:], aux)
            output[ii]= aux2*puw.unit(tmp_length_unit, __quantities_form__)**3
        return output

def minimum_image_convention(item, selection='all', reference_selection=None,
                             reference_coordinates=None, center_of_selection='geometrical_center',
                             center_of_reference_selection='geometrical_center', frame_indices='all',
                             syntaxis='MDTraj', engine='MolSysMT'):

    from molsysmt import convert, select, get, duplicate
    from molsysmt import set as _set
    from molsysmt.tools.math import serialized_lists
    from molsysmt.centers import geometrical_center

    n_atoms, n_frames = get(item, n_atoms=True, n_frames=True)
    atom_indices = select(item, selection=selection, syntaxis=syntaxis)
    n_atom_indices = len(atom_indices)
    frame_indices = _digest_frame_indices(item, frame_indices)
    n_frame_indices = len(frame_indices)

    engine = _digest_engines(engine)
    form_in, _ = _digest_forms(item, engine)
    tmp_item = duplicate(item)

    if engine=='MolSysMT':

        if reference_coordinates is None:
            if center_of_reference_selection == 'geometrical_center':
                reference_coordinates = geometrical_center(tmp_item, selection=reference_selection,
                                                        frame_indices=frame_indices, syntaxis=syntaxis, engine=engine)

        molecules = get(tmp_item, molecules=True)

        if selection not in [None, 'all']:
            working_molecules = []
            for molecule in molecules:
                if len(_np.intersect1d(molecule, atom_indices)):
                    working_molecules.append(molecule)
            molecules=working_molecules

        molecules_serialized = serialized_lists(molecules, dtype='int64')

        if center_of_selection == 'geometrical_center':
            centers_molecules = geometrical_center(tmp_item, selection_groups=molecules,
                    frame_indices=frame_indices, syntaxis=syntaxis, engine=engine)

        coordinates, box, box_shape = get(tmp_item, coordinates=True, box=True, box_shape=True, frame_indices='all')

        length_units = coordinates.unit
        coordinates = _np.asfortranarray(coordinates._value, dtype='float64')
        reference_coordinates = _np.asfortranarray(reference_coordinates._value, dtype='float64')
        box = _np.asfortranarray(box._value, dtype='float64')
        orthogonal = 0
        if box_shape=='cubic': orthogonal = 1

        _libbox.minimum_image_convention(coordinates, reference_coordinates, centers_molecules,
                molecules_serialized.indices, molecules_serialized.values,
                molecules_serialized.starts, frame_indices, box, orthogonal,
                n_frames, n_atoms, molecules_serialized.n_indices, molecules_serialized.n_values,
                n_frame_indices)

        coordinates=_np.ascontiguousarray(coordinates)*length_units

        _set(tmp_item, coordinates=coordinates)

        del(coordinates, box, length_units)
        del(molecules, molecules_serialized)

        return tmp_item

    else:

        raise NotImplementedError

def unwrap_molecules_from_pbc_cell(item, selection='all', frame_indices='all', syntaxis='MDTraj', engine='MolSysMT'):

    from molsysmt import convert, select, get, duplicate
    from molsysmt import set as _set
    from molsysmt.tools.math import serialized_lists

    n_atoms, n_frames = get(item, n_atoms=True, n_frames=True)
    atom_indices = select(item, selection=selection, syntaxis=syntaxis)
    n_atom_indices = len(atom_indices)
    frame_indices = _digest_frame_indices(item, frame_indices)
    n_frame_indices = len(frame_indices)

    engine = _digest_engines(engine)
    form_in, _ = _digest_forms(item, engine)
    tmp_item = duplicate(item)

    if engine=='MolSysMT':

        molecules = get(tmp_item, molecules=True)

        if selection not in [None, 'all']:
            working_molecules = []
            for molecule in molecules:
                if len(_np.intersect1d(molecule, atom_indices)):
                    working_molecules.append(molecule)
            molecules=working_molecules

        molecules_serialized = serialized_lists(molecules, dtype='int64')

        bonded_atoms = get(tmp_item, target='atom', indices=atom_indices, bonded_atoms=True)
        bonded_atoms_serialized = serialized_lists(bonded_atoms, dtype='int64')

        coordinates, box, box_shape = get(tmp_item, coordinates=True, box=True, box_shape=True, frame_indices='all')

        length_units = coordinates.unit
        coordinates = _np.asfortranarray(coordinates._value, dtype='float64')
        box = _np.asfortranarray(box._value, dtype='float64')
        orthogonal = 0
        if box_shape=='cubic': orthogonal = 1

        _libbox.unwrap(coordinates, molecules_serialized.indices, molecules_serialized.values, molecules_serialized.starts,
                       bonded_atoms_serialized.indices, bonded_atoms_serialized.values, bonded_atoms_serialized.starts,
                       frame_indices, box, orthogonal, n_frames, n_atoms,
                       molecules_serialized.n_indices, molecules_serialized.n_values,
                       bonded_atoms_serialized.n_indices, bonded_atoms_serialized.n_values,
                       n_frame_indices)

        coordinates=_np.ascontiguousarray(coordinates)*length_units

        _set(tmp_item, coordinates=coordinates)

        del(coordinates, box, length_units)
        del(molecules, molecules_serialized, bonded_atoms, bonded_atoms_serialized)

        return tmp_item

    else:

        raise NotImplementedError

def wrap_molecules_to_pbc_cell(self):
    #self.coors=asfortran_np.array(self.coors)
    #libbox.wrap_all_inplace(self.coors,self.box,self.invbox,self.orthogonal,self.coors.shape[0])
    #self.coors=ascontiguous_np.array(self.coors)
    raise NotImplementedError

