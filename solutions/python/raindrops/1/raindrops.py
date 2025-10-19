def convert(number):
    """Convert a number into its raindrop sounds.
    
    Rules:
    - Divisible by 3 → add "Pling"
    - Divisible by 5 → add "Plang"
    - Divisible by 7 → add "Plong"
    - Not divisible by any → return the number as string
    
    :param number: int - positive integer to convert.
    :return: str - raindrop sounds or the number as string.
    
    Examples:
    >>> convert(28)
    'Plong'
    >>> convert(30)
    'PlingPlang'
    >>> convert(34)
    '34'
    >>> convert(105)
    'PlingPlangPlong'
    """
    result = ""
    
    # Check divisibility by 3
    if number % 3 == 0:
        result += "Pling"
    
    # Check divisibility by 5
    if number % 5 == 0:
        result += "Plang"
    
    # Check divisibility by 7
    if number % 7 == 0:
        result += "Plong"
    
    # If no sounds were added, return the number as string
    if not result:
        result = str(number)
    
    return result