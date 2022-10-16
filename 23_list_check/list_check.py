def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    t_f = []
    for item in lst:
        if type(item) == list:
            t_f.append(True)
    if len(lst) == len(t_f):
        return True
    else:
        return False