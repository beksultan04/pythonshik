def value(colors):
    """Calculate the two-digit numeric value from resistor color bands.
    
    Takes the first two color bands and converts them to a two-digit number.
    Additional colors beyond the first two are ignored.
    
    :param colors: list - list of color names.
    :return: int - two-digit resistance value.
    
    Examples:
    >>> value(["brown", "green"])
    15
    >>> value(["brown", "green", "violet"])
    15
    >>> value(["orange", "orange"])
    33
    >>> value(["black", "black"])
    0
    >>> value(["blue", "grey"])
    68
    """
    # Color to number mapping
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    
    # Get the first two colors only
    first_color = colors[0]
    second_color = colors[1]
    
    # Convert to digits
    first_digit = color_map[first_color]
    second_digit = color_map[second_color]
    
    # Combine into two-digit number
    return first_digit * 10 + second_digit