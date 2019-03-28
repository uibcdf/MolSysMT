import numpy as _np
from simtk import unit as _unit
from molmodmt.lib import box as _libbox
from molmodmt.utils.exceptions import *
from copy import deepcopy

# Tiene que haber una manera automatica con f2py dar siempre de salida Ccontiguous_np.arrays

class Trajectory():

    def __init__(self, filename=None):

        self.filename = None
        self.coordinates = None # ndarray with shape=(n_frames, n_atoms, 3) and dtype=float
                                # and order=F, with units nanometers
        self.box   = None # ndarray with shape=(n_frames,3,3), dtype=float and order='F'
        self.cell  = None # ndarray with shape=(n_frames,3,3), dtype=float and order='F'
        self.timestep  = None
        self.integstep  = None
        self.step  = None
        self.time  = None
        self.model = None # In case it is a model and not a timestep
        self.nframes = 0
        self.natoms = 0

        self.invbox       = None #_np.zeros(shape=(n_frames,3,3),dtype=float,order='F')
        self.orthogonal   = 0
        self.volume       = 0.0

        self.topology = None
        self.topology_mdtraj = None
        self.selection_mdtraj = None
        self._atoms_list_mdtraj = None
        self.topography = None
        self.structure = None

        self._length_units = _unit.nanometers
        self._time_units     = _unit.picoseconds

        self.filename = filename

    def _import_mdtraj_data(self,item=None):

        from .io_trajectory import parse_mdtraj_Trajectory
        tmp_coordinates, tmp_box, tmp_time, tmp_timestep = parse_mdtraj_Trajectory(item)
        self._initialize_with_coors(coordinates=tmp_coordinates, box=tmp_box, timestep=tmp_timestep,
                                    time=tmp_time)
        pass

    def _import_mdtraj_topology(self,item=None):
        self.topology_mdtraj=item.topology
        pass

    def _initialize_with_coors(self, coordinates=None, box=None, cell=None, timestep=None, integstep=None,
                 step=None, time=None):

        self.coordinates = coordinates
        self.box   = box
        self.cell  = cell
        self.timestep  = timestep
        self.integstep  = integstep
        self.step  = step
        self.time  = time

        if self.coordinates is not None:
            self.nframes = self.coordinates.shape[0]
            self.natoms = self.coordinates.shape[1]

        ii = self.coordinates
        if ii is not None:
            if _np.isfortran(ii)==False:
                ii=_np.asfortranarray(ii)

        ii = self.box
        if ii is not None:
            if _np.isfortran(ii)==False:
                ii=_np.asfortranarray(ii)

        ii = self.cell
        if ii is not None:
            if _np.isfortran(ii)==False:
                ii=_np.asfortranarray(ii)

        ii = self.time
        if ii is not None:
            if _np.isfortran(ii)==False:
                ii=_np.asfortranarray(ii)

        ii = self.step
        if ii is not None:
            if _np.isfortran(ii)==False:
                ii=_np.asfortranarray(ii)

        if (self.cell is None) and (self.box is not None):
            self.box2cell()

        if (self.cell is not None) and (self.box is None):
            self.cell2box()

        if (self.box is not None):
            self.box2invbox()

        pass

    def cell2box(self):
        self.box,self.volume,self.orthogonal=_libbox.cell2box(self.cell, self.nframes)
        pass

    def box2cell(self):
        self.cell,self.volume,self.orthogonal=_libbox.box2cell(self.box, self.nframes)
        pass

    def box2invbox(self):
        self.invbox=_libbox.box2invbox(self.box, self.nframes)
        pass

    def unwrap(self,selection=None,min_image_selection=None,syntaxis='mdtraj'):

        from molmodmt import select as _select
        from molmodmt import get_molecules as _get_molecules
        from molmodmt.utils.fortran import listoflists2fortran as _listoflists2fortran

        molecules, bonds = _get_molecules(self.topology_mdtraj,with_bonds=True)

        if selection is not None:
            atoms_list = _select(self.topology_mdtraj,selection,syntaxis)
            molecules2unwrap = []
            for molecule in molecules:
                if len(_np.intersect1d(molecule,atoms_list)):
                    molecules2unwrap.append(molecule)
            molecules=molecules2unwrap

        molecules_array_all, molecules_array_starts = _listoflists2fortran(molecules,dtype='int64')
        bonds_array_all, bonds_array_starts = _listoflists2fortran(bonds,dtype='int64')

        self.coordinates=_np.asfortranarray(self.coordinates,dtype='float64')
        self.box=_np.asfortranarray(self.box,dtype='float64')
        self.invbox=_np.asfortranarray(self.invbox,dtype='float64')
        _libbox.unwrap(self.coordinates, molecules_array_all,
                       molecules_array_starts, bonds_array_all, bonds_array_starts,
                       self.box, self.invbox, self.orthogonal,
                       self.nframes, self.natoms,
                       molecules_array_all.shape[0], molecules_array_starts.shape[0],
                       bonds_array_all.shape[0], bonds_array_starts.shape[0])

        self.coordinates=_np.ascontiguousarray(self.coordinates)
        self.box=_np.ascontiguousarray(self.box)
        self.invbox=_np.ascontiguousarray(self.invbox)
        pass

    def wrap(self):
        #self.coors=asfortran_np.array(self.coors)
        #libbox.wrap_all_inplace(self.coors,self.box,self.invbox,self.orthogonal,self.coors.shape[0])
        #self.coors=ascontiguous_np.array(self.coors)
        pass

    def extract(self,selection=None):  # Extract new frame complete frame from selection
        #tmp_frame=deepcopy(self)
        #tmp_frame.coors=tmp_frame.coors[selection,:]
        #return tmp_frame
        pass

    def iterload(self,chunk=100, stride=1, skip=0, selection=None, syntaxis='mdtraj'):

        atoms_list = None

        if selection is None:
            if self.selection_mdtraj is not None:
                atoms_list = self._atoms_list_mdtraj
        else:
            from molmodmt.multitool import select as _select
            atoms_list = _select(self.topology_mdtraj,selection,syntaxis)

        from mdtraj import iterload as _mdtraj_iterload
        tmp_top = self.topology_mdtraj

        iterator = _mdtraj_iterload(self.filename, top=tmp_top, chunk=chunk,
                                                stride=stride, atom_indices=atoms_list)

        while True:
            tmp_mdtraj = next(iterator)
            if tmp_mdtraj is None:
                return
            self._import_mdtraj_data(tmp_mdtraj)
            if atoms_list is not None:
                self._import_mdtraj_topology(tmp_mdtrajectory)
            del(tmp_mdtraj)
            yield

    def load(self,frame=None,selection=None,syntaxis='mdtraj'):

        from mdtraj import load as _mdtraj_load
        from mdtraj import join as _mdtraj_join
        from mdtraj import load_frame as _mdtraj_load_frame
        from .io_topology import to_mdtraj_Topology as _to_mdtraj_Topology
        from numpy import ndarray

        tmp_top = self.topology_mdtraj
        mdtraj_read = False
        atoms_list = None

        if selection is None:
            if self.selection_mdtraj is not None:
                atoms_list = self._atoms_list_mdtraj
        else:
            from molmodmt.multitool import select as _select
            atoms_list = _select(self.topology_mdtraj,selection,syntaxis)

        if type(frame)==str:
            if frame.lower()=='all':
                tmp_mdtrajectory = _mdtraj_load(self.filename,top=tmp_top,atom_indices=atoms_list)
                mdtraj_read = True
        elif type(frame)==int:
            tmp_mdtrajectory = _mdtraj_load_frame(self.filename,frame,top=tmp_top,atom_indices=atoms_list)
            mdtraj_read = True
        elif type(frame) in [list,tuple,ndarray]:
            mdtraj_read = True
            tmp_trajs=[]
            for ii in range(0,len(frame)):
                tmp_trajs.append(_mdtraj_load_frame(self.filename, frame[ii],top=tmp_top, atom_indices=atoms_list))
            tmp_mdtrajectory=_mdtraj_join(tmp_trajs,check_topology=False)
            del(tmp_trajs)

        if mdtraj_read:
            self._import_mdtraj_data(tmp_mdtrajectory)
            if atoms_list is not None:
                self._import_mdtraj_topology(tmp_mdtrajectory)
        else:
            raise BadCallError(BadCallMessage)
