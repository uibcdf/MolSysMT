from os.path import basename as _basename
from simtk.openmm.app import Simulation as _openmm_Simulation

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _openmm_Simulation : form_name,
    'openmm.Simulation' : form_name,
}

info=["",""]
with_topology=True
with_coordinates=False
with_box=False
with_parameters=True

def to_molsysmt_Topology(item, atom_indices='all', frame_indices='all',
                         topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.topology.classes import from_openmm_Simulation as openmm_Simulation_to_molsysmt_Topology
    tmp_item = openmm_Simulation_to_molsysmt_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_molsysmt_Trajectory(item, atom_indices='all', frame_indices='all',
                           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.trajectory.classes import from_openmm_Simulation as openmm_Simulation_to_molsysmt_Trajectory
    tmp_item = openmm_Simulation_to_molsysmt_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_molsysmt_MolSys(item, atom_indices='all', frame_indices='all',
                       topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.molsys.classes import from_openmm_Simulation as openmm_Simulation_to_molsysmt_MolSys
    tmp_item = openmm_Simulation_to_molsysmt_MolSys(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_openmm_Topology(item, atom_indices='all', frame_indices='all',
                       topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    tmp_item=item.topology
    tmp_item=extract(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_openmm_Modeller(item, atom_indices='all', frame_indices='all',
                       topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from simtk.openmm.app import Modeller
    topology = to_openmm_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    positions = get_coordinates_from_atom(item, indices=atom_indices, frame_indices=frame_indices)
    tmp_item = Modeller(topology, positions)
    return tmp_item

def to_openmm_Context(item, atom_indices='all', frame_indices='all',
                      topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    return item.context

def to_pdbfixer_PDBFixer(item, atom_indices='all', frame_indices='all',
                         topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt._private_tools.pdb import tmp_pdb_filename
    from molsysmt.forms.files.api_pdb import to_pdbfixer_PDBFixer as pdb_to_pdbfixer_PDBFixer
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filename=tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = pdb_to_pdbfixer_PDBFixer(tmp_file)
    remove(tmp_pdbfile)
    return tmp_item

def to_pdb (item, atom_indices='all', frame_indices='all',
            topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None,
            output_filename=None):

    from .api_openmm_Topology import to_pdb as openmm_Topology_to_pdb

    topology = to_openmm_Topology(item, atom_indices=atom_indices)
    coordinates = get_coordinates_from_atom(item, indices=atom_indices, frame_indices=frame_indices)
    box = get_box_from_system(item, frame_indices=frame_indices)
    topology.setPeriodicBoxVectors(box)
    return openmm_Topology_to_pdb(topology, output_filename=output_filename, trajectory_item=coordinates)

def extract(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def copy(item):

    raise NotImplementedError

###### Get

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    state = item.context.getState(getPositions=True)
    coordinates = state.getPositions(asNumpy=True)
    if indices is not 'all':
        coordinates = coordinates[indices,:]
    return coordinates

## system

def get_coordinates_from_system(item, indices='all', frame_indices='all'):

    state = item.context.getState(getPositions=True)
    coordinates = state.getPositions(asNumpy=True)
    return coordinates

def get_box_from_system(item, indices='all', frame_indices='all'):

    state = item.context.getState()
    box = state.getPeriodicBoxVectors()
    return box

def get_form_from_system(item, indices='all', frame_indices='all'):

    return form_name

