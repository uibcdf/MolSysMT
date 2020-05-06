from os.path import basename as _basename

form_name=_basename(__file__).split('.')[0].split('_')[-1]


is_form = {
    'smi': form_name,
    'SMI': form_name
    }

info=["",""]
with_topology=True
with_trajectory=False

def extract(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def copy(item):

    raise NotImplementedError

###### Get

## system

def get_form_from_system(item, indices='all', frame_indices='all'):

    return form_name

