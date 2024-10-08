"""
Unit and regression test for the convert module of the molsysmt package.
"""

# Import package, test suite, and other packages as needed
import molsysmt as msm
from molsysmt import systems
import numpy as np
import os

# Whole systems (selection='all' and structure_indices='all')

def test_file_pdb_to_mdtraj_Trajectory():
    molsys = systems['T4 lysozyme L99A']['181l.pdb']
    molsys = msm.convert(molsys, to_form='mdtraj.Trajectory')
    form = msm.get_form(molsys)
    assert 'mdtraj.Trajectory'==form

def test_file_pdb_to_openmm_Topology():
    molsys = systems['T4 lysozyme L99A']['181l.pdb']
    molsys = msm.convert(molsys, to_form='openmm.Topology')
    form = msm.get_form(molsys)
    assert 'openmm.Topology'==form

def test_file_pdb_to_string_pdb_text():
    molsys = systems['T4 lysozyme L99A']['181l.pdb']
    molsys = msm.convert(molsys, to_form='string:pdb_text')
    form = msm.get_form(molsys)
    assert 'string:pdb_text'==form

def test_file_pdb_to_pdbfixer_PDBFixer():
    molsys = systems['T4 lysozyme L99A']['181l.pdb']
    molsys = msm.convert(molsys, to_form='pdbfixer.PDBFixer')
    form = msm.get_form(molsys)
    assert 'pdbfixer.PDBFixer'==form

def test_file_pdb_to_parmed_Structure():
    molsys = systems['T4 lysozyme L99A']['181l.pdb']
    molsys = msm.convert(molsys, to_form='parmed.Structure')
    form = msm.get_form(molsys)
    assert 'parmed.Structure'==form

def test_file_pdb_to_molsysmt_MolSys_1():
    molsys = systems['chicken villin HP35']['1vii.pdb']
    molsys = msm.convert(molsys)
    form = msm.get_form(molsys)
    box = msm.get(molsys, box=True)
    assert 'molsysmt.MolSys'==form
    assert box is None


