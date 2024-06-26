Elements
-------------------------

The fundamental elements are atoms, groups, components, molecules, entities and bioassemblies. They act as
building blocks of superior elements, defining this way hierarchical organization levels of a
molecular model. A bioassembly is composed by entities with one or more molecules. A molecule is composed by
components, a component by groups, and finnaly a by atoms.

```
atom ---> group ---> component ---> molecule ---> entities ---> bioassembly
                         |                           ^
                         |                           |
                         ---------> chain ------------
```

## Atom

Atoms are the indivisible element of a classical molecular model.

Refer api

## Group

Sets of atoms are sometimes defined as building block elements of more complex structures. This is
the case of aminoacids and nucleotides. This is then the immediately superior hierarchical level
over "atoms".

Refer api :class:`molsysmt.native.elements.atom`

## Component

Components are composed by one or many groups, and thereby by one or many atoms.
Components are uniquely defined as the set of atoms, and groups, covalently bonded.
The name "component" is taken from graph or network theory where the "components" of a graph or a
network are the connected set of nodes (any node of a component is connected by at least a path of edges to any
other node of the same component). 
Thereby, a polymer made by nucleotides or aminoacids is a component, no matter is a fragment of a protein or one of the strands of a DNA fragment. And in coherence with this definition, an ion, a water molecule or a small molecules are also components.

## Molecule

A molecule is composed by one or many components. A protein quaternary structure is composed by more than a polymer of
aminoacids, more than a component. In the same way a fragment of DNA is composed by two nucleotides
strands (components). While a peptide or a single folded protein are made by a single component.
And in coherence with this definition, an ion or a water molecule are perse a molecules composed by
single components.

## Chains

Chains are ambiguously defined. Chain, as thy can be found in the protein data bank, are sets of components for sure. But it can not be
said that chains are composed always by molecules or that molecules are composed always by chains.
A set of molecules can sometimes define a chain (e.g.: crystal waters), or a molecule can be made up by more than a chain (e.g.: protein complex).

## Entities

Entities are set of molecules defined by the same molecular nature. Water is an entity made by all
water molecules in the bioassembly, e.g. Or Urea can be another entity present in the molecular
model, or "Epstein Barr Nuclear Antigen 1" or "Trypanosoma Cruzi Triosephosphate Isomerase", no
matter the number of molecules of each nature can be found in the molecular model.

