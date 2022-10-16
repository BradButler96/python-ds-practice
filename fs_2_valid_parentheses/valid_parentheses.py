def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    paren_len = len(parens)
    half_len = int(paren_len / 2)
    half1 = parens[:half_len]
    half2 = parens[half_len:]
    if parens[0] == ')':
        return False
    elif len(parens) % 2 != 0:
        return False
    else:
        list2 = list(half2)
        for i in range(len(list2)):
            if list2[i] == '(':
                list2[i] = ')'
            elif list2[i] == ')':
                list2[i] = '('
        flipped2 = ''.join(list2)
        if half1 == flipped2[::-1]:
            return True