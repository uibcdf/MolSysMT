from mendeleev import element as _element
from .utils.engines import digest as _digest_engines

## https://mendeleev.readthedocs.io/en/stable/
## https://github.com/lmmentel/mendeleev

def get_atomic_electronegativity(item, scale='pauling', selection='all', syntaxis='MDTraj', engine='mendeleev'):

    # https://mendeleev.readthedocs.io/en/stable/data.html#electronegativities

    engine = _digest_engines(engine)

    if engine=='mendeleev':

        from molmodmt import get

        en_selection=[]

        selection_elements = get(item, target='atom', selection=selection, syntaxis=syntaxis, element=True)
        unique_elements = list(set(selection_elements))
        en_elements = {}
        for element_symbol in unique_elements:
            element = _element(element_symbol)
            if scale in ["gosh"]:
                en_elements[element_symbol] = element.en_gosh
            else:
                en_elements[element_symbol] = element.electronegativity(scale)
        for element_symbol in selection_elements:
            en_selection.append(en_elements[element_symbol])

        return en_selection

    else:

        raise NotImplementedError(NotImplementedMessage)

    pass

