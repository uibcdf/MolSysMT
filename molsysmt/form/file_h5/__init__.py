from .is_file_h5 import is_file_h5

from .extract import extract
from .add import add
from .append_structures import append_structures
from .get import *
from .set import *
from .iterators import StructuresIterator, TopologyIterator

from .to_mdtraj_HDF5TrajectoryFile import to_mdtraj_HDF5TrajectoryFile
from .to_molsysmt_MolSys import to_molsysmt_MolSys
from .to_molsysmt_Topology import to_molsysmt_Topology
from .to_molsysmt_Structures import to_molsysmt_Structures
from .to_nglview_NGLWidget import to_nglview_NGLWidget
from .to_openmm_Topology import to_openmm_Topology
from .to_mdtraj_Topology import to_mdtraj_Topology
from .to_mdtraj_Trajectory import to_mdtraj_Trajectory
from .to_file_pdb import to_file_pdb
