def has_cosolutes(molecular_system):

    from molsysmt.basic import get

    output = False

    n_cosolutes = get(molecular_system, target='system', n_cosolutes=True)

    if n_cosolutes>0:
        output = True

    return output
