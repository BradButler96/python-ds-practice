def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    str = ''
    lst = list(phrase)
    new_lst = []
    to_swap = to_swap.lower()
    for letter in lst:
        if letter == to_swap:
            new_letter = letter.upper()
            new_lst.append(new_letter)
        elif letter == to_swap.upper():
            new_letter = letter.lower()
            new_lst.append(new_letter)
        else:
            new_lst.append(letter)
    return str.join(new_lst)
