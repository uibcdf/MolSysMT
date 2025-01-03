form_name = 'file:gro'
form_type = 'file'
form_info = ["Gromacs gro file format",
             "http://manual.gromacs.org/documentation/2018/user-guide/file-formats.html#gro"]

piped_topological_attribute = 'molsysmt.MolSys'
piped_structural_attribute = 'molsysmt.Structure'
piped_any_attribute = 'molsysmt.MolSys'
bonds_are_explicit = False
bonds_can_be_computed = True

from .is_form import is_form

from .attributes import attributes
from .has_attribute import has_attribute

from .extract import extract
from .copy import copy
from .add import add
from .merge import merge
from .append_structures import append_structures
from .get import *
from .set import *
from .iterators import StructuresIterator, TopologyIterator

from .to_mdtraj_Trajectory import to_mdtraj_Trajectory
from .to_mdtraj_Topology import to_mdtraj_Topology
from .to_mdtraj_GroTrajectoryFile import to_mdtraj_GroTrajectoryFile
from .to_molsysmt_MolSys import to_molsysmt_MolSys
from .to_molsysmt_Topology import to_molsysmt_Topology
from .to_molsysmt_Structures import to_molsysmt_Structures
from .to_molsysmt_GROFileHandler import to_molsysmt_GROFileHandler
from .to_openmm_Topology import to_openmm_Topology
from .to_openmm_Modeller import to_openmm_Modeller
from .to_openmm_GromacsGroFile import to_openmm_GromacsGroFile
from .to_nglview_NGLWidget import to_nglview_NGLWidget

_convert_to={
        'file:gro': extract,
        'mdtraj.Trajectory': to_mdtraj_Trajectory,
        'mdtraj.Topology': to_mdtraj_Topology,
        'mdtraj.GroTrajectoryFile': to_mdtraj_GroTrajectoryFile,
        'molsysmt.MolSys': to_molsysmt_MolSys,
        'molsysmt.Topology': to_molsysmt_Topology,
        'molsysmt.Structures': to_molsysmt_Structures,
        'molsysmt.GROFileHandler': to_molsysmt_GROFileHandler,
        'openmm.Topology': to_openmm_Topology,
        'openmm.Modeller': to_openmm_Modeller,
        'openmm.GromacsGroFile': to_openmm_GromacsGroFile,
        'nglview.NGLWidget': to_nglview_NGLWidget,
        }

