def reverse(text):
    """Reverse a given string.
    
    :param text: str - string to reverse.
    :return: str - reversed string.
    
    Examples:
    >>> reverse("stressed")
    'desserts'
    >>> reverse("strops")
    'sports'
    >>> reverse("racecar")
    'racecar'
    >>> reverse("Hello, World!")
    '!dlroW ,olleH'
    """
    # Python's slice notation with step -1 reverses the string
    return text[::-1]