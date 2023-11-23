from molsysmt._private.digestion import digest

@digest(form='MDAnalysis.Universe')
def to_molsysmt_StructuresOld(item, atom_indices='all', structure_indices='all'):

    from molsysmt.native.structures_old import StructuresOld
    from . import get_coordinates_from_atom, get_structure_id_from_system, get_time_from_system, get_box_from_system

    tmp_item = StructuresOld()

    coordinates = get_coordinates_from_atom(item, indices=atom_indices, structure_indices=structure_indices)
    structure_id = get_structure_id_from_system(item, structure_indices=structure_indices)
    time = get_time_from_system(item, structure_indices=structure_indices)
    box = get_box_from_system(item, structure_indices=structure_indices)

    tmp_item.append_structures(structure_id=structure_id, time=time, coordinates=coordinates, box=box)

    return tmp_item
