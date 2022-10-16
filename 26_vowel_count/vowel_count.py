def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    vowels = 'aeiou'
    vowels_in_phrase = []
    for char in phrase:
        if char in vowels:
            vowels_in_phrase.append(char)
    count = dict()
    for vowel in vowels_in_phrase:
        count[vowel] = count.get(vowel,0) +1
    print(count)