from .small_molecule_names import small_molecule_names

def is_small_molecule(name):

    return (name in small_molecule_names)
