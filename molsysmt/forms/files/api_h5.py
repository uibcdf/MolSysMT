from os.path import basename as _basename

form_name=_basename(__file__).split('.')[0].split('_')[-1]

is_form = {
    'h5': form_name,
    'hdf5': form_name
    }

info=["",""]
with_topology=True
with_trajectory=True

def to_mdtraj_Trajectory(item, atom_indices='all', frame_indices='all',
                         topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from mdtraj import load_hdf5 as mdtraj_load_hdf5
    tmp_item = mdtraj_load_hdf5(item)
    return tmp_item

def to_mdtraj_Topology(item, atom_indices='all', frame_indices='all',
                       topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    tmp_item2 = tmp_item.topology
    tmp_item.close()
    del(tmp_item)
    return tmp_item2

def to_mdtraj_HDF5TrajectoryFile(item, atom_indices='all', frame_indices='all',
                                 topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from mdtraj.formats import HDF5TrajectoryFile
    return HDF5TrajectoryFile(item)

def to_openmm_Topology(item, atom_indices='all', frame_indices='all',
                       topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    tmp_item = to_mdtraj_Topology(item)
    tmp_item = tmp_item.to_openmm()
    return tmp_item

def to_molsysmt_MolSys(item, atom_indices='all', frame_indices='all',
                       topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.molsys.files import from_h5 as h5_to_molsysmt_MolSys
    tmp_item = h5_to_molsysmt_MolSys(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_molsysmt_Topology(item, atom_indices='all', frame_indices='all',
                         topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.topology.files import from_h5 as h5_to_molsysmt_Topology
    tmp_item = h5_to_molsysmt_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_molsysmt_Trajectory(item, atom_indices='all', frame_indices='all',
                           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.trajectory.files import from_h5 as h5_to_molsysmt_Trajectory
    return h5_to_molsysmt_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)

def to_pdb(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None,
           output_filename=None):

    from molsysmt.forms.classes.api_molsysmt_MolSys import to_pdb as molsysmt_MolSys_to_pdb
    tmp_item = to_molsysmt_MolSys(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return molsysmt_MolSys_to_pdb(tmp_item, output_filename=output_filename)

def extract(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def copy(item, output_filename=None):

    from shutil import copyfile

    er=copyfile(item, output_filename)
    pass

def to_NGLView(item, atom_indices='all', frame_indices='all',
               topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.forms.classes.api_molsysmt_MolSys import to_NGLView as convert
    tmp_item = to_molsysmt_MolSys(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return convert(tmp_item)

#### Get

def get_frames_from_atom (item, indices='all', frame_indices='all'):

    from molsysmt import get
    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    xyz, time, step, box = get(tmp_item, target='atom', indices=indices,
                               frame_indices=frame_indices, frames=True)
    tmp_item.close()
    del(tmp_item, get)
    return xyz, time, step, box

# System

def get_frames_from_system (item, indices='all', frame_indices='all'):

    from molsysmt import get
    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    xyz, time, step, box = get(tmp_item, target='system',
            frame_indices=frame_indices, frames=True)
    tmp_item.close()
    del(tmp_item, get)
    return xyz, time, step, box

def get_n_frames_from_system (item, indices='all', frame_indices='all'):

    from molsysmt import get
    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    n_frames = get(tmp_item, target='system',  n_frames=True)
    tmp_item.close()
    del(tmp_item, get)
    return n_frames

def get_n_atoms_from_system (item, indices='all', frame_indices='all'):

    from molsysmt import get
    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    n_atoms = get(tmp_item, target='system',  n_atoms=True)
    tmp_item.close()
    del(tmp_item, get)
    return n_atoms

def get_form_from_system(item, indices='all', frame_indices='all'):

    return form_name

