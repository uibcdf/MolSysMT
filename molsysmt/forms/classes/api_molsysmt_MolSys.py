from os.path import basename as _basename
from molsysmt._private_tools.exceptions import *
from molsysmt import MolSys as _molsysmt_MolSys
import simtk.unit as unit

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molsysmt_MolSys : form_name,
    'molsysmt.MolSys': form_name
}

info=["",""]
with_topology=True
with_coordinates=True
with_box=True
with_parameters=False

def to_molsysmt_Topology(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.molsys.classes import to_molsysmt_Topology as molsysmt_MolSys_to_molsysmt_Topology
    return molsysmt_MolSys_to_molsysmt_Topology(item)

def to_molsysmt_Trajectory(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.molsys.classes import to_molsysmt_Trajectory as molsysmt_MolSys_to_molsysmt_Trajectory
    return molsysmt_MolSys_to_molsysmt_Trajectory(item)

def to_XYZ(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.molsys.classes import to_XYZ as molsysmt_MolSys_to_XYZ
    return molsysmt_MolSys_to_XYZ(item)

def to_aminoacids3_seq(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from .api_molsysmt_Topology import to_aminoacids3_seq as molsysmt_topology_to_aminoacids3_seq
    tmp_item = molsysmt_topology_to_aminoacids3_seq(item.topology, atom_indices=atom_indices,
                                                      frame_indices=frame_indices)
    return tmp_item

def to_aminoacids1_seq(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from .api_molsysmt_Topology import to_aminoacids1_seq as molsysmt_topology_to_aminoacids1_seq
    tmp_item = molsysmt_topology_to_aminoacids1_seq(item.topology,
                                                      frame_indices=frame_indices)

    return tmp_item

def to_biopython_Seq(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.forms.seqs.api_aminoacids1 import to_biopython_Seq as aminoacids1_to_biopython_Seq
    tmp_item = to_aminoacids1_seq(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = aminoacids1_to_biopython_Seq(tmp_item)
    return tmp_item

def to_biopython_SeqRecord(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.forms.seqs.api_aminoacids1 import to_biopython_SeqRecord as aminoacids1_to_biopython_SeqRecord
    tmp_item = to_aminoacids1_seq(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = aminoacids1_to_biopython_SeqRecord(tmp_item)
    return tmp_item

def to_mdtraj_Trajectory(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.molsys.classes import to_mdtraj_Trajectory as molsysmt_MolSys_to_mdtraj_Trajectory

    tmp_item = molsysmt_MolSys_to_mdtraj_Trajectory(item, atom_indices=atom_indices,
                                                   frame_indices=frame_indices)

    return tmp_item

def to_mdtraj_Topology(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from .api_molsysmt_Topology import to_mdtraj_Topology as molsysmt_Topology_to_mdtraj_Topology
    return molsysmt_Topology_to_mdtraj_Topology(item.topology, atom_indices=atom_indices,
                                                frame_indices=frame_indices)

def to_openmm_Topology(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.molsys.classes import to_openmm_Topology as molsysmt_MolSys_to_openmm_Topology
    tmp_item = molsysmt_MolSys_to_openmm_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_openmm_Modeller(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.molsys.classes import to_openmm_Modeller as molsysmt_MolSys_to_openmm_Modeller
    tmp_item = molsysmt_MolSys_to_openmm_Modeller(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_openmm_System(item, atom_indices='all', frame_indices='all',
        topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None,
        forcefield=None, non_bonded_method='no_cutoff', non_bonded_cutoff=1.0*unit.nanometer, constraints=None,
        rigid_water=True, remove_cm_motion=True, hydrogen_mass=None, switch_distance=None,
        flexible_constraints=False):

    from molsysmt.native.io.molsys.classes import to_openmm_System as molsysmt_MolSys_to_openmm_System

    tmp_item = molsysmt_MolSys_to_openmm_System(item, atom_indices=atom_indices, frame_indices=frame_indices,
        forcefield=forcefield, non_bonded_method=non_bonded_method, non_bonded_cutoff=non_bonded_cutoff, constraints=constraints,
        rigid_water=rigid_water, remove_cm_motion=remove_cm_motion, hydrogen_mass=hydrogen_mass, switch_distance=switch_distance,
        flexible_constraints=flexible_constraints)

    return tmp_item

def to_openmm_Simulation(item, atom_indices='all', frame_indices='all',
        topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None,
        forcefield=None, non_bonded_method='no_cutoff', non_bonded_cutoff=None, constraints=None,
        rigid_water=True, remove_cm_motion=True, hydrogen_mass=None, switch_distance=None,
        flexible_constraints=False, integrator='Langevin', temperature=300.0*unit.kelvin,
        collisions_rate=1.0/unit.picoseconds, integration_timestep=2.0*unit.femtoseconds, platform='CUDA'):

    from molsysmt.native.io.molsys.classes import to_openmm_Simulation as molsysmt_MolSys_to_openmm_Simulation

    if trajectory_item is None:
        trajectory_item = item

    tmp_item = molsysmt_MolSys_to_openmm_Simulation(item, trajectory_item=trajectory_item, atom_indices=atom_indices, frame_indices=frame_indices,
            forcefield=forcefield, non_bonded_method=non_bonded_method, non_bonded_cutoff=non_bonded_cutoff, constraints=constraints,
            rigid_water=rigid_water, remove_cm_motion=remove_cm_motion, hydrogen_mass=hydrogen_mass, switch_distance=switch_distance,
            flexible_constraints=flexible_constraints, integrator=integrator,
            temperature=temperature, collisions_rate=collisions_rate, integration_timestep=integration_timestep, platform=platform)

    return tmp_item

def to_pdb(item, atom_indices='all', frame_indices='all',
           topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None,
           output_filename=None):

    from molsysmt.native.io.molsys.files import to_pdb as molsysmt_MolSys_to_pdb
    return molsysmt_MolSys_to_pdb(item, output_filename=output_filename, atom_indices=atom_indices,
                                  frame_indices=frame_indices)

def to_pdbfixer_PDBFixer(item, atom_indices='all', frame_indices='all',
                         topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from molsysmt.native.io.molsys.classes import to_pdbfixer_PDBFixer as molsysmt_MolSys_to_pdbfixer_PDBFixer

    tmp_item = molsysmt_MolSys_to_pdbfixer_PDBFixer(item, trajectory_item=trajectory_item,
                                                    atom_indices=atom_indices,
                                                    frame_indices=frame_indices)
    return tmp_item

def select_with_MDTraj(item, selection):

    from .api_molsysmt_Topology import select_with_MDTraj as select_Topology_with_MDTraj
    return select_Topology_with_MDTraj(item.topology, selection)

def select_with_MolSysMT(item, selection):

    from .api_molsysmt_Topology import select_with_MolSysMT as select_Topology_with_MolSysMT
    return select_Topology_with_MolSysMT(item.topology, selection)

def extract(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        return item.extract(atom_indices=atom_indices, frame_indices=frame_indices)

def to_nglview_NGLView(item, atom_indices='all', frame_indices='all',
                       topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    from nglview import show_molsysmt
    tmp_view = show_molsysmt(item, selection=atom_indices, frame_indices=frame_indices)
    return tmp_view

def to_NGLView(item, atom_indices='all', frame_indices='all',
              topology_item=None, trajectory_item=None, coordinates_item=None, box_item=None):

    return to_NGLView(item, atom_indices=atom_indices, frame_indices=frame_indices)

def copy(item):

    return item.copy()

def merge(list_items, list_atom_indices, list_frame_indices):

    from molsysmt.native.molsys import MolSys

    tmp_item = MolSys()

    for item, atom_indices, frame_indices in zip(list_items, list_atom_indices, list_frame_indices):
        tmp_item.add(item, selection=atom_indices, frame_indices=frame_indices)

    return tmp_item

def concatenate(list_items, list_atom_indices, list_frame_indices):

    from molsysmt.native.molsys import MolSys

    tmp_item = MolSys()

    tmp_item.add(list_items[0], selection=list_atom_indices[0], frame_indices=list_frame_indices[0])

    for item, atom_indices, frame_indices in zip(list_items[1:], list_atom_indices[1:], list_frame_indices[1:]):

        step, time, coordinates, box = get_frame_from_atom(item, indices=atom_indices, frame_indices=frame_indices)
        tmp_item.trajectory.append_frames(step, time, coordinates, box)

    return tmp_item

def add(item, list_items, list_atom_indices, list_frame_indices):

    for aux_item, aux_atom_indices, aux_frame_indices in zip(list_items, list_atom_indices, list_frame_indices):

        item.add(aux_item, selection=aux_atom_indices, frame_indices=aux_frame_indices)

    pass

def append(item, list_items, list_atom_indices, list_frame_indices):

    for aux_item, aux_atom_indices, aux_frame_indices in zip(list_items, list_atom_indices, list_frame_indices):

        step, time, coordinates, box = get_frame_from_atom(aux_item, indices=aux_atom_indices, frame_indices=aux_frame_indices)
        item.trajectory.append_frames(step, time, coordinates, box)

    pass

###### Get

## atom

def get_index_from_atom (item, indices='all', frame_indices='all'):

    return get_atom_index_from_atom(item, indices=indices, frame_indices=frame_indices)

def get_id_from_atom (item, indices='all', frame_indices='all'):

    return get_atom_id_from_atom(item, indices=indices, frame_indices=frame_indices)

def get_name_from_atom (item, indices='all', frame_indices='all'):

    return get_atom_name_from_atom(item, indices=indices, frame_indices=frame_indices)

def get_type_from_atom (item, indices='all', frame_indices='all'):

    return get_atom_type_from_atom(item, indices=indices, frame_indices=frame_indices)

def get_atom_index_from_atom(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_id_from_atom(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_id_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_name_from_atom(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_name_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_type_from_atom(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_type_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_id_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_id_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_name_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_name_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_type_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_type_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_name_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_name_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_id_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_id_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_type_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_type_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_name_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_name_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_id_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_id_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_type_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_type_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_id_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_id_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_name_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_name_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_type_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_type_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_id_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_id_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_name_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_name_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_type_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_type_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_atoms_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_atoms_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_groups_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_groups_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_components_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_components_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_molecules_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_molecules_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_chains_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_chains_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_entities_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_entities_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_bonded_atoms_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_bonded_atoms_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_bond_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_bond_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_bonds_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_inner_bond_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_inner_bond_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_inner_bonded_atoms_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_inner_bonded_atoms_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_inner_bonds_from_atom (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_inner_bonds_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_mass_from_atom(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_mass_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_charge_from_atom(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_charge_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_coordinates_from_atom as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_frame_from_atom(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_frame_from_atom as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_n_frames_from_atom(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_n_frames_from_atom as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_form_from_atom(item, indices='all', frame_indices='all'):

    return form_name

## group

def get_index_from_group (item, indices='all', frame_indices='all'):

    return get_group_index_from_group (item, indices=indices, frame_indices=frame_indices)

def get_id_from_group (item, indices='all', frame_indices='all'):

    return get_group_id_from_group (item, indices=indices, frame_indices=frame_indices)

def get_name_from_group (item, indices='all', frame_indices='all'):

    return get_group_name_from_group (item, indices=indices, frame_indices=frame_indices)

def get_type_from_group (item, indices='all', frame_indices='all'):

    return get_group_type_from_group (item, indices=indices, frame_indices=frame_indices)

def get_atom_index_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_index_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_id_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_id_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_name_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_name_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_type_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_type_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_index_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_index_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_id_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_id_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_name_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_name_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_type_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_type_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_name_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_name_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_index_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_index_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_id_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_id_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_type_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_type_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_name_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_name_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_index_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_index_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_id_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_id_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_type_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_type_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_index_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_index_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_id_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_id_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_name_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_name_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_type_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_type_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_index_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_index_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_id_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_id_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_name_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_name_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_type_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_type_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_atoms_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_atoms_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_groups_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_groups_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_components_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_components_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_molecules_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_molecules_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_chains_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_chains_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_entities_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_entities_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_group (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_bonds_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_mass_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_mass_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_charge_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_charge_from_group as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_coordinates_from_group(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_coordinates_from_group as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

## component

def get_index_from_component (item, indices='all', frame_indices='all'):

    return get_component_index_from_component (item, indices=indices, frame_indices=frame_indices)

def get_id_from_component (item, indices='all', frame_indices='all'):

    return get_component_id_from_component (item, indices=indices, frame_indices=frame_indices)

def get_name_from_component (item, indices='all', frame_indices='all'):

    return get_component_name_from_component (item, indices=indices, frame_indices=frame_indices)

def get_type_from_component (item, indices='all', frame_indices='all'):

    return get_component_type_from_component (item, indices=indices, frame_indices=frame_indices)

def get_atom_index_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_index_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_id_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_id_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_name_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_name_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_type_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_type_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_index_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_index_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_id_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_id_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_name_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_name_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_type_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_type_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_name_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_name_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_index_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_index_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_id_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_id_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_type_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_type_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_name_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_name_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_index_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_index_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_id_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_id_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_type_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_type_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_index_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_index_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_id_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_id_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_name_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_name_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_type_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_type_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_index_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_index_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_id_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_id_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_name_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_name_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_type_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_type_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_atoms_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_atoms_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_groups_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_groups_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_components_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_components_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_molecules_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_molecules_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_chains_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_chains_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_entities_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_entities_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_component (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_bonds_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_mass_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_mass_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_charge_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_charge_from_component as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_coordinates_from_component(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_coordinates_from_component as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)


## molecule

def get_index_from_molecule (item, indices='all', frame_indices='all'):

    return get_molecule_index_from_molecule (item, indices=indices, frame_indices=frame_indices)

def get_id_from_molecule (item, indices='all', frame_indices='all'):

    return get_molecule_id_from_molecule (item, indices=indices, frame_indices=frame_indices)

def get_name_from_molecule (item, indices='all', frame_indices='all'):

    return get_molecule_name_from_molecule (item, indices=indices, frame_indices=frame_indices)

def get_type_from_molecule (item, indices='all', frame_indices='all'):

    return get_molecule_type_from_molecule (item, indices=indices, frame_indices=frame_indices)

def get_atom_index_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_index_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_id_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_id_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_name_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_name_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_type_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_type_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_index_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_index_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_id_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_id_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_name_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_name_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_type_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_type_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_name_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_name_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_index_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_index_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_id_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_id_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_type_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_type_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_name_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_name_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_index_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_index_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_id_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_id_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_type_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_type_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_index_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_index_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_id_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_id_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_name_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_name_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_type_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_type_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_index_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_index_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_id_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_id_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_name_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_name_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_type_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_type_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_atoms_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_atoms_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_groups_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_groups_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_components_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_components_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_molecules_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_molecules_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_chains_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_chains_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_entities_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_entities_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_molecule (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_bonds_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_mass_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_mass_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_charge_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_charge_from_molecule as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_coordinates_from_molecule(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_coordinates_from_molecule as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)


## chain

def get_index_from_chain (item, indices='all', frame_indices='all'):

    return get_chain_index_from_chain (item, indices=indices, frame_indices=frame_indices)

def get_id_from_chain (item, indices='all', frame_indices='all'):

    return get_chain_id_from_chain (item, indices=indices, frame_indices=frame_indices)

def get_name_from_chain (item, indices='all', frame_indices='all'):

    return get_chain_name_from_chain (item, indices=indices, frame_indices=frame_indices)

def get_type_from_chain (item, indices='all', frame_indices='all'):

    return get_chain_type_from_chain (item, indices=indices, frame_indices=frame_indices)

def get_atom_index_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_index_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_id_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_id_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_name_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_name_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_type_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_type_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_index_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_index_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_id_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_id_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_name_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_name_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_type_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_type_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_name_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_name_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_index_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_index_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_id_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_id_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_type_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_type_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_name_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_name_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_index_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_index_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_id_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_id_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_type_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_type_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_index_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_index_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_id_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_id_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_name_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_name_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_type_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_type_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_index_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_index_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_id_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_id_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_name_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_name_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_type_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_type_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_atoms_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_atoms_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_groups_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_groups_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_components_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_components_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_molecules_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_molecules_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_chains_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_chains_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_entities_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_entities_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_chain (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_bonds_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_mass_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_mass_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_charge_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_charge_from_chain as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_coordinates_from_chain(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_coordinates_from_chain as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

## entity

def get_index_from_entity (item, indices='all', frame_indices='all'):

    return get_entity_index_from_entity (item, indices=indices, frame_indices=frame_indices)

def get_id_from_entity (item, indices='all', frame_indices='all'):

    return get_entity_id_from_entity (item, indices=indices, frame_indices=frame_indices)

def get_name_from_entity (item, indices='all', frame_indices='all'):

    return get_entity_name_from_entity (item, indices=indices, frame_indices=frame_indices)

def get_type_from_entity (item, indices='all', frame_indices='all'):

    return get_entity_type_from_entity (item, indices=indices, frame_indices=frame_indices)

def get_atom_index_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_index_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_id_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_id_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_name_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_name_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_type_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_type_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_index_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_index_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_id_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_id_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_name_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_name_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_group_type_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_group_type_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_name_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_name_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_index_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_index_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_id_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_id_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_component_type_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_component_type_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_name_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_name_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_index_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_index_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_id_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_id_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_type_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_chain_type_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_index_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_index_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_id_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_id_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_name_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_name_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecule_type_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_molecule_type_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_index_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_index_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_id_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_id_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_name_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_name_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_entity_type_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_entity_type_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_atoms_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_atoms_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_groups_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_groups_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_components_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_components_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_molecules_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_molecules_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_chains_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_chains_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_entities_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_entities_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_entity (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_bonds_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_mass_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_mass_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_charge_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_charge_from_entity as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_coordinates_from_entity(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_coordinates_from_entity as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)


## system

def get_bonded_atoms_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_bonded_atoms_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_atoms_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_groups_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_groups_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_components_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_components_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_chains_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_chains_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_molecules_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_molecules_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_entities_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_entities_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_bonds_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_aminoacids_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_aminoacids_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_nucleotides_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_nucleotides_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_ions_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_ions_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_waters_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_waters_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_cosolutes_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_cosolutes_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_small_molecules_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_small_molecules_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_peptides_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_peptides_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_proteins_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_proteins_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_dnas_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_dnas_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_rnas_from_system (item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_dnas_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_mass_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_mass_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_charge_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_mass_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_coordinates_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_coordinates_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_box_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_box_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_box_shape_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_box_shape_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_box_lengths_from_system(item, indices='all', frame_indices='all'):

    tmp_box_lengths = item.trajectory.get_box_lengths()
    if tmp_box_lengths is not None and frame_indices is not 'all':
        tmp_box_lengths = tmp_box_lengths[frame_indices,:]
    return tmp_box_lengths

def get_box_angles_from_system(item, indices='all', frame_indices='all'):

    tmp_box_angles = item.trajectory.get_box_angles()
    if tmp_box_angles is not None and frame_indices is not 'all':
        tmp_box_angles = tmp_box_angles[frame_indices,:]
    return tmp_box_angles

def get_box_volume_from_system(item, indices='all', frame_indices='all'):

    from molsysmt.pbc import box_volume_from_box_vectors
    tmp_box = get_box_from_system(item, indices=indices, frame_indices=frame_indices)
    return box_volume_from_box_vectors(tmp_box)

def get_time_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_time_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_step_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_step_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_frame_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_frame_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_n_frames_from_system(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Trajectory import get_n_frames_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_form_from_system(item, indices='all', frame_indices='all'):

    return form_name

def get_has_topology_from_system(item, indices='all', frame_indices='all'):

    return True

def get_has_parameters_from_system(item, indices='all', frame_indices='all'):

    return False

def get_has_box_from_system(item, indices='all', frame_indices='all'):

    tmp_box = get_box_from_system(item, indices=indices, frame_indices=frame_indices)
    if tmp_box[0] is not None:
        return True
    else:
        return False

def get_has_coordinates_from_system(item, indices='all', frame_indices='all'):

    return True

def get_has_bonds_from_system(item, indices='all', frame_indices='all'):

    if get_n_bonds_from_system(item, indices=indices, frame_indices=frame_indices):
        return True
    else:
        return False

## bond

def get_index_from_bond(item, indices='all', frame_indices='all'):

    return get_bond_index_from_bond(item, indices=indices)

def get_order_from_bond(item, indices='all', frame_indices='all'):

    return get_bond_order_from_bond(item, indices=indices)

def get_type_from_bond(item, indices='all', frame_indices='all'):

    return get_bond_type_from_bond(item, indices=indices)

def get_bond_index_from_bond(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_bond_index_from_bond as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_bond_order_from_bond(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_bond_order_from_bond as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_bond_type_from_bond(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_bond_type_from_bond as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_atom_index_from_bond(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_atom_index_from_bond as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_bond(item, indices='all', frame_indices='all'):

    from .api_molsysmt_Topology import get_n_bonds_from_bond as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

###### Set

def set_box_to_system(item, indices='all', frame_indices='all', value=None):

    item.trajectory.box = value
    pass

def set_coordinates_to_system(item, indices='all', frame_indices='all', value=None):

    item.trajectory.coordinates = value
    pass

