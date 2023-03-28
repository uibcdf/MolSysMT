from molsysmt._private.digestion import digest

@digest(form='openmm.AmberPrmtopFile')
def has_attribute(molecular_system, attribute):

    from . import attributes

    output = attributes[attribute]

    return output
