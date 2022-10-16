def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    key_lst = list(d.keys())
    if type(key_lst[0]) == int:
        new_d = dict([(value, key) for key, value in d.items()])
        max_val = max(new_d.values())
        min_val = min(new_d.values())
        return (min_val, max_val)
    else:
        d_vals = list(d.values())
        dup = [x for i, x in enumerate(d_vals) if i != d_vals.index(x)]
        dup_val = dup[0]
        dup_keys = [k for k,v in d.items() if v == dup_val]
        dup_tup = tuple(dup_keys)
        return dup_tup
