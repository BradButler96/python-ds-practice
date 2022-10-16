def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here
    word = word.lower()
    nums = range(1,27)
    letters = list('abcdefghijklmnopqrstuvwxyz')
    val_key = {letters[i - 1]: i for i in nums}
    sum = 0
    for char in word:
        sum += val_key[char]
    if sum % 2 != 0:
        return True
    else:
        return False