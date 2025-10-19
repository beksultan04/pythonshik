def is_pangram(sentence):
    """Determine if a sentence is a pangram.
    
    A pangram contains every letter of the alphabet at least once.
    Case insensitive - 'a' and 'A' count as the same letter.
    
    :param sentence: str - sentence to check.
    :return: bool - True if pangram, False otherwise.
    
    Examples:
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("abcdefghijklmnopqrstuvwxyz")
    True
    >>> is_pangram("Hello World")
    False
    >>> is_pangram("")
    False
    """
    # Define the complete alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    # Convert sentence to lowercase and get unique letters
    sentence_letters = set(sentence.lower())
    
    # Check if all alphabet letters are present in the sentence
    return alphabet <= sentence_letters


# Alternative approaches:

def is_pangram_v2(sentence):
    """Alternative using issubset()."""
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(sentence.lower())


def is_pangram_v3(sentence):
    """Alternative using all() and in."""
    sentence_lower = sentence.lower()
    return all(letter in sentence_lower for letter in 'abcdefghijklmnopqrstuvwxyz')


def is_pangram_v4(sentence):
    """Alternative using string.ascii_lowercase."""
    import string
    return set(string.ascii_lowercase) <= set(sentence.lower())