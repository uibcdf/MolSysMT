from molsysmt._private.digestion import digest

@digest(form='molsysmt.Structures')
def to_molsysmt_StructuresDict(item, atom_indices='all', structure_indices='all', skip_digestion=False):

    from . import get_coordinates_from_atom, get_structure_id_from_system, get_time_from_system, get_box_from_system

    coordinates = get_coordinates_from_atom(item, indices=atom_indices, structure_indices=structure_indices,
                                            skip_digestion=True)
    structure_id = get_structure_id_from_system(item, structure_indices=structure_indices, skip_digestion=True)
    time = get_time_from_system(item, structure_indices=structure_indices, skip_digestion=True)
    box = get_box_from_system(item, structure_indices=structure_indices, skip_digestion=True)

    tmp_item = {}

    if structure_id is not None:
        tmp_item['structure_id']=structure_id

    if time is not None:
        tmp_item['time']=time

    if coordinates is not None:
        tmp_item['coordinates']=coordinates

    if box is not None:
        tmp_item['box']=box

    return tmp_item

