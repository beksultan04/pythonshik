def square(number):
    """Calculate the number of grains on a given square.
    
    Square 1 has 1 grain (2^0)
    Square 2 has 2 grains (2^1)
    Square 3 has 4 grains (2^2)
    And so on, doubling each time.
    
    :param number: int - square number (1-64).
    :return: int - number of grains on that square.
    :raises ValueError: if number is not between 1 and 64.
    
    Examples:
    >>> square(1)
    1
    >>> square(2)
    2
    >>> square(3)
    4
    >>> square(16)
    32768
    """
    # Validate input
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    # Each square has 2^(n-1) grains
    # Square 1: 2^0 = 1
    # Square 2: 2^1 = 2
    # Square 3: 2^2 = 4
    return 2 ** (number - 1)


def total():
    """Calculate the total number of grains on all 64 squares.
    
    This is the sum of grains on squares 1 through 64.
    Sum = 2^0 + 2^1 + 2^2 + ... + 2^63
    
    Using the formula for sum of geometric series:
    Sum = 2^64 - 1
    
    :return: int - total number of grains on the chessboard.
    
    Example:
    >>> total()
    18446744073709551615
    """
    # Sum of geometric series: 2^0 + 2^1 + ... + 2^63 = 2^64 - 1
    return 2 ** 64 - 1
    
    # Alternative approach (less efficient but more explicit):
    # return sum(square(n) for n in range(1, 65))