from os.path import basename as _basename
from molsysmt._private_tools.exceptions import *
from molsysmt.native.trajectory import Trajectory as _molsysmt_Trajectory
import numpy as np

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molsysmt_Trajectory : form_name,
    'molsysmt.Trajectory' : form_name
}

info=["",""]
with_topology=False

with_parameters=False

# Methods

def to_mdtraj_Trajectory(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.trajectory.classes import to_mdtraj_Trajectory as molsysmt_Trajectory_to_mdtraj_Trajectory
    return molsysmt_Trajectory_to_mtraj_Trajectory(item, selection=atom_indices, frame_indices=frame_indices, syntaxis=syntaxis)

def to_parmed_GromacsTopologyFile(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from .api_mdtraj_Topology import to_parmed_GromacsTopologyFile as mdtraj_Topology_to_parmed_GromacsTopologyFile
    tmp_item = to_mdtraj_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return mdtraj_Topology_to_GromacsTopologyFile(tmp_item)

def to_xtc(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None,
           output_filename=None):

    from .api_mdtraj_Trajectory import to_xtc as mdtraj_Trajectory_to_xtc
    tmp_item=to_mdtraj_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return mdtraj_Trajectory_to_xtc(tmp_item, output_filename=output_filename)

def to_top(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None,
           output_filename=None):

    from .api_mdtraj_Topology import to_top as mdtraj_Topology_to_top
    tmp_item = to_mdtraj_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return mdtraj_Topology_to_top(tmp_item, output_filename=output_filename)

def select_with_MDTraj(item, selection):
    from .api_mdtraj_Topology import select_with_MDTraj as _select_with_MDTraj
    return _select_with_MDTraj(item.topology_mdtraj,selection)

def to_NGLView(item, atom_indices='all', frame_indices='all'):

    raise NotImplementedError

def extract(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        return item.extract(atom_indices=atom_indices, frame_indices=frame_indices)

def copy(item):

    return item.copy()

def merge_two_items(item1, item2):

    tmp_item = copy(item1)
    tmp_item.add(item2)
    return tmp_item

###### Get

## atom

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    tmp_coordinates = item.coordinates

    if frame_indices is not 'all':
        tmp_coordinates = tmp_coordinates[frame_indices,:,:]

    if indices is not 'all':
        tmp_coordinates = tmp_coordinates[:,indices,:]

    return tmp_coordinates

def get_n_atoms_from_atom(item, indices='all', frame_indices='all'):

    if indices is 'all':
        output=item.coordinates.shape[1]
    else:
        output=indices.shape[0]

    return output

def get_frame_from_atom(item, indices='all', frame_indices='all'):

    tmp_step = get_step_from_system(item, frame_indices=frame_indices)
    tmp_time = get_time_from_system(item, frame_indices=frame_indices)
    tmp_coordinates = get_coordinates_from_atom(item, indices=indices, frame_indices=frame_indices)
    tmp_box = get_box_from_system(item, frame_indices=frame_indices)

    return tmp_step, tmp_time, tmp_coordinates, tmp_box

def get_n_frames_from_atom(item, indices='all', frame_indices='all'):

    return get_n_frames_from_system(item, indices='all', frame_indices='all')

## system

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    if indices is 'all':
        output=item.coordinates.shape[1]
    else:
        output=indices.shape[0]

    return output

def get_coordinates_from_system(item, indices='all', frame_indices='all'):

    if frame_indices is 'all':
        output=item.coordinates
    else:
        output=item.coordinates[frame_indices,:,:]
    return output

def get_box_from_system(item, indices='all', frame_indices='all'):

    output=None
    if item.box is not None:
        if frame_indices is 'all':
            output=item.box
        else:
            output=item.box[frame_indices,:,:]
    return output

def get_box_shape_from_system(item, indices='all', frame_indices='all'):

    return item.box_shape

def get_box_lengths_from_system(item, indices='all', frame_indices='all'):

    tmp_box_lengths = item.get_box_lengths()
    if frame_indices is 'all':
        output = tmp_box_lengths
    else:
        output = tmp_box_lengths[frame_indices,:]
    return output

def get_box_angles_from_system(item, indices='all', frame_indices='all'):

    tmp_box_angles = item.get_box_angles()
    if frame_indices is 'all':
        output = tmp_box_angles
    else:
        output = tmp_box_angles[frame_indices,:]
    return output

def get_time_from_system(item, indices='all', frame_indices='all'):

    if frame_indices is 'all':
        output = item.time
    else:
        output = item.time[frame_indices]
    return output

def get_step_from_system(item, indices='all', frame_indices='all'):

    if frame_indices is 'all':
        output = item.step
    else:
        output = item.step[frame_indices]
    return output

def get_frame_from_system(item, indices='all', frame_indices='all'):

    tmp_step = get_step_from_system(item, frame_indices=frame_indices)
    tmp_time = get_time_from_system(item, frame_indices=frame_indices)
    tmp_coordinates = get_coordinates_from_system(item, frame_indices=frame_indices)
    tmp_box = get_box_from_system(item, frame_indices=frame_indices)

    return tmp_step, tmp_time, tmp_coordinates, tmp_box

def get_n_frames_from_system(item, indices='all', frame_indices='all'):

    if frame_indices is 'all':
        output=item.coordinates.shape[0]
    else:
        output=frame_indices.shape[0]

    return output

def get_form_from_system(item, indices='all', frame_indices='all'):

    return form_name

###### Set

def set_box_to_system(item, indices='all', frame_indices='all', value=None):

    n_frames_trajectory = item.coordinates.shape[0]
    n_frames_box = value.shape[0]

    if n_frames_trajectory == n_frames_box:
        item.box = value
    else:
        if n_frames_box == 1:
            item.box = np.broadcast_to(value[0]._value, (n_frames_trajectory,3,3)) * value.unit
        else:
            raise ValueError("box and coordinates have different shape")

    pass

def set_coordinates_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError

