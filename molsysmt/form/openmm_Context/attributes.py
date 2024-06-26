from molsysmt.attribute.attributes import attributes as _all_attributes

attributes = {ii:False for ii in _all_attributes}

attributes['n_atoms'] = True
attributes['atom_index'] = True
attributes['n_structures'] = True
attributes['coordinates'] = True
attributes['velocities'] = True
attributes['box'] = True
attributes['time'] = True
attributes['structure_id'] = True
attributes['temperature'] = True

del(_all_attributes)
