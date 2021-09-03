"""
Unit and regression test for the compare module of the molsysmt package.
"""

# Import package, test suite, and other packages as needed
import molsysmt as msm
import numpy as np

def test_compare_all_eq_1():
    molsys_A = msm.demo.classes.T4_Lysozyme_L99A_in_pdbid_181l(to_form='molsysmt.MolSys')
    molsys_B = msm.demo.classes.T4_Lysozyme_L99A_in_pdbid_181l(to_form='molsysmt.MolSys')
    output = msm.compare(molsys_A, molsys_B, comparison='all', rule='A_eq_B')
    assert output == True

def test_compare_all_eq_2():
    molsys_A = msm.demo.classes.valine_dipeptide_vacuum(to_form='molsysmt.MolSys')
    molsys_B = msm.demo.classes.lysine_dipeptide_vacuum(to_form='molsysmt.MolSys')
    output = msm.compare(molsys_A, molsys_B, comparison='all', rule='A_eq_B')
    assert output == False

