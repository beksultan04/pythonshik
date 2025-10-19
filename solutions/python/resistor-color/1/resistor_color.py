def color_code(color):
    """Return the numeric value associated with a resistor color band.
    
    :param color: str - color name.
    :return: int - numeric value (0-9).
    
    Examples:
    >>> color_code("black")
    0
    >>> color_code("white")
    9
    >>> color_code("orange")
    3
    """
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
    return color_map[color]


def colors():
    """Return the list of all color band names in order.
    
    :return: list - ordered list of color names.
    
    Example:
    >>> colors()
    ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    """
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]