def is_element(element):

    from molsysmt.element import _elements, _plural_elements_to_singular

    output = False

    if element in _plural_elements_to_singular:
        output = True

    elif element in _elements:
        output = True

    return output

