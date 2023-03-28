"""
Unit and regression test for the convert module of the molsysmt package.
"""

# Import package, test suite, and other packages as needed
import molsysmt as msm
from molsysmt.basic.convert import _convert_multiple_to_one_with_shortcuts, _convert_multiple_to_one
import numpy as np
import os

def test_convert_file_prmtop_and_file_inpcrd_to_molsysmt_MolSys():
    prmtop_file = msm.demo['pentalanine']['pentalanine.prmtop']
    inpcrd_file = msm.demo['pentalanine']['pentalanine.inpcrd']
    molsys = msm.convert([prmtop_file, inpcrd_file], to_form='molsysmt.MolSys')
    form = msm.get_form(molsys)
    n_atoms, n_structures, box = msm.get(molsys, n_atoms=True, n_structures=True, box=True)
    n_atoms_prmtop = msm.get(prmtop_file, n_atoms=True)
    n_structures_inpcrd, box_inpcrd = msm.get(inpcrd_file, n_structures=True, box=True)
    assert 'molsysmt.MolSys'==form
    assert n_atoms==n_atoms_prmtop
    assert n_structures==n_structures_inpcrd
    assert np.allclose(box, box_inpcrd)

def test_convert_file_prmtop_and_file_inpcrd_to_molsysmt_MolSys_2():
    prmtop_file = msm.demo['pentalanine']['pentalanine.prmtop']
    inpcrd_file = msm.demo['pentalanine']['pentalanine.inpcrd']
    molsys = _convert_multiple_to_one_with_shortcuts([prmtop_file, inpcrd_file], to_form='molsysmt.MolSys')
    form = msm.get_form(molsys)
    n_atoms, n_structures, box = msm.get(molsys, n_atoms=True, n_structures=True, box=True)
    n_atoms_prmtop = msm.get(prmtop_file, n_atoms=True)
    n_structures_inpcrd, box_inpcrd = msm.get(inpcrd_file, n_structures=True, box=True)
    assert 'molsysmt.MolSys'==form
    assert n_atoms==n_atoms_prmtop
    assert n_structures==n_structures_inpcrd
    assert np.allclose(box, box_inpcrd)

def test_convert_file_prmtop_and_file_inpcrd_to_molsysmt_MolSys_3():
    prmtop_file = msm.demo['pentalanine']['pentalanine.prmtop']
    inpcrd_file = msm.demo['pentalanine']['pentalanine.inpcrd']
    molsys = _convert_multiple_to_one([prmtop_file, inpcrd_file], to_form='molsysmt.MolSys')
    form = msm.get_form(molsys)
    n_atoms, n_structures, box = msm.get(molsys, n_atoms=True, n_structures=True, box=True)
    n_atoms_prmtop = msm.get(prmtop_file, n_atoms=True)
    n_structures_inpcrd, box_inpcrd = msm.get(inpcrd_file, n_structures=True, box=True)
    assert 'molsysmt.MolSys'==form
    assert n_atoms==n_atoms_prmtop
    assert n_structures==n_structures_inpcrd
    assert np.allclose(box, box_inpcrd)

def test_convert_file_psf_and_file_dcd_to_molsysmt_MolSys():
    psf_file = msm.demo['membrane']['membrane.psf']
    dcd_file = msm.demo['membrane']['membrane.dcd']
    molsys = msm.convert([psf_file, dcd_file], to_form='molsysmt.MolSys')
    form = msm.get_form(molsys)
    n_atoms, n_structures = msm.get(molsys, n_atoms=True, n_structures=True)
    assert 'molsysmt.MolSys'==form
    assert n_atoms==78974
    assert n_structures==50

def test_convert_file_psf_and_file_dcd_to_molsysmt_MolSys_2():
    psf_file = msm.demo['membrane']['membrane.psf']
    dcd_file = msm.demo['membrane']['membrane.dcd']
    molsys = _convert_multiple_to_one_with_shortcuts([psf_file, dcd_file], to_form='molsysmt.MolSys')
    form = msm.get_form(molsys)
    n_atoms, n_structures = msm.get(molsys, n_atoms=True, n_structures=True)
    assert 'molsysmt.MolSys'==form
    assert n_atoms==78974
    assert n_structures==50

def test_convert_file_psf_and_file_dcd_to_molsysmt_MolSys_3():
    psf_file = msm.demo['membrane']['membrane.psf']
    dcd_file = msm.demo['membrane']['membrane.dcd']
    molsys = _convert_multiple_to_one([psf_file, dcd_file], to_form='molsysmt.MolSys')
    form = msm.get_form(molsys)
    n_atoms, n_structures = msm.get(molsys, n_atoms=True, n_structures=True)
    assert 'molsysmt.MolSys'==form
    assert n_atoms==78974
    assert n_structures==50

def test_convert_file_gro_and_file_xtc_to_molsysmt_MolSys():
    molsys_1 = msm.demo['nglview']['md_1u19.gro']
    molsys_2 = msm.demo['nglview']['md_1u19.xtc']
    molsys = msm.convert([molsys_1, molsys_2], to_form='molsysmt.MolSys')
    form = msm.get_form(molsys)
    assert 'molsysmt.MolSys'==form

def test_convert_file_gro_and_file_xtc_to_molsysmt_MolSys_2():
    molsys_1 = msm.demo['nglview']['md_1u19.gro']
    molsys_2 = msm.demo['nglview']['md_1u19.xtc']
    molsys = _convert_multiple_to_one_with_shortcuts([molsys_1, molsys_2], to_form='molsysmt.MolSys')
    form = msm.get_form(molsys)
    assert 'molsysmt.MolSys'==form

def test_convert_file_gro_and_file_xtc_to_molsysmt_MolSys_3():
    molsys_1 = msm.demo['nglview']['md_1u19.gro']
    molsys_2 = msm.demo['nglview']['md_1u19.xtc']
    molsys = _convert_multiple_to_one([molsys_1, molsys_2], to_form='molsysmt.MolSys')
    form = msm.get_form(molsys)
    assert 'molsysmt.MolSys'==form