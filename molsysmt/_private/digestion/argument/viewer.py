from molsysmt._private.exceptions import ArgumentError
from molsysmt.engine.engines import viewers

viewer_from_lowercase = {ii.lower(): ii for ii in viewers}

def digest_viewer(viewer, caller=None):
    """ Check if the given viewer is supported by MolSysMT.

    Parameters
    ----------
    viewer : str
        The name of the viewer in lowercase.

    Returns
    -------

    Raises
    -------

    """
    try:
        tmp_viewer = viewer_from_lowercase[viewer.lower()]
        return tmp_viewer
    except KeyError:
        raise ArgumentError('viewer', caller=caller, message=None)
