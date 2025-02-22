form_name = 'file:prmtop'
form_type = 'file'
form_info = ["AMBER parameter/topology file format",
             "https://ambermd.org/FileFormats.php#topology"]

piped_topological_attribute = 'molsysmt.Topology'
piped_structural_attribute = None
piped_any_attribute = None
bonds_are_explicit = True
bonds_can_be_computed = False

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

from .to_file_pdb import to_file_pdb
from .to_mdtraj_Topology import to_mdtraj_Topology
from .to_molsysmt_MolSys import to_molsysmt_MolSys
from .to_molsysmt_Topology import to_molsysmt_Topology
from .to_nglview_NGLWidget import to_nglview_NGLWidget
from .to_openmm_AmberPrmtopFile import to_openmm_AmberPrmtopFile
from .to_openmm_Modeller import to_openmm_Modeller
from .to_openmm_Topology import to_openmm_Topology

_convert_to={
        'file:prmtop': extract,
        'file:pdb': to_file_pdb,
        'mdtraj.Topology': to_mdtraj_Topology,
        'molsysmt.MolSys': to_molsysmt_MolSys,
        'molsysmt.Topology': to_molsysmt_Topology,
        'nglview.NGLWidget': to_nglview_NGLWidget,
        'openmm.AmberPrmtopFile': to_openmm_AmberPrmtopFile,
        'openmm.Modeller': to_openmm_Modeller,
        'openmm.Topology': to_openmm_Topology,
        }
