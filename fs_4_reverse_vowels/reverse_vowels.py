from operator import inv


def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiou'
    s = list(s)
    s_copy = s.copy()
    vowel_idx = [index for index, char in enumerate(s) if char.lower() in vowels]
    vowel_idx_copy = vowel_idx.copy()
    inv_idx = vowel_idx_copy[::-1]
    vowel_idx_range = range(int(len(vowel_idx) / 2))
    for i in vowel_idx_range:
        s[vowel_idx[i]] = s_copy[inv_idx[i]]
        s[inv_idx[i]] = s_copy[vowel_idx[i]]
    return ''.join(s)