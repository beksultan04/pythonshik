def rotate(text, key):
    """Encode text using a rotational cipher (Caesar cipher).
    
    Shifts each letter by 'key' positions in the alphabet.
    Preserves case, spaces, punctuation, and numbers.
    
    :param text: str - text to encode.
    :param key: int - rotation key (0-26).
    :return: str - encoded text.
    
    Examples:
    >>> rotate("omg", 5)
    'trl'
    >>> rotate("c", 0)
    'c'
    >>> rotate("Cool", 26)
    'Cool'
    >>> rotate("The quick brown fox jumps over the lazy dog.", 13)
    'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'
    """
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            if char.isupper():
                # Shift within uppercase letters (A-Z)
                # A = 65, Z = 90 in ASCII
                shifted = ((ord(char) - ord('A') + key) % 26) + ord('A')
                result.append(chr(shifted))
            else:
                # Shift within lowercase letters (a-z)
                # a = 97, z = 122 in ASCII
                shifted = ((ord(char) - ord('a') + key) % 26) + ord('a')
                result.append(chr(shifted))
        else:
            # Keep non-letter characters unchanged
            result.append(char)
    
    return ''.join(result)