def is_isogram(string):
    """Determine if a word or phrase is an isogram.
    
    An isogram has no repeating letters (case insensitive).
    Spaces and hyphens don't count as letters and can repeat.
    
    :param string: str - word or phrase to check.
    :return: bool - True if isogram, False otherwise.
    
    Examples:
    >>> is_isogram("lumberjacks")
    True
    >>> is_isogram("background")
    True
    >>> is_isogram("downstream")
    True
    >>> is_isogram("six-year-old")
    True
    >>> is_isogram("isograms")
    False
    >>> is_isogram("eleven")
    False
    """
    # Convert to lowercase for case-insensitive comparison
    string_lower = string.lower()
    
    # Extract only letters (ignore spaces, hyphens, etc.)
    letters_only = [char for char in string_lower if char.isalpha()]
    
    # Check if number of unique letters equals total number of letters
    # If they're equal, no letter repeats
    return len(letters_only) == len(set(letters_only))


# Alternative approaches:

def is_isogram_v2(string):
    """Alternative using filter."""
    letters = filter(str.isalpha, string.lower())
    letters_list = list(letters)
    return len(letters_list) == len(set(letters_list))


def is_isogram_v3(string):
    """Alternative checking for duplicates explicitly."""
    letters = [char.lower() for char in string if char.isalpha()]
    return len(letters) == len(set(letters))


def is_isogram_v4(string):
    """Alternative using Counter to check for repeats."""
    from collections import Counter
    letters = [char.lower() for char in string if char.isalpha()]
    letter_counts = Counter(letters)
    return all(count == 1 for count in letter_counts.values())