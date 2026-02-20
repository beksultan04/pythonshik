def is_valid(isbn):
    """Validate an ISBN-10 number.
    
    ISBN-10 format: 9 digits + 1 check character (digit or X)
    Validation formula: (d₁*10 + d₂*9 + ... + d₁₀*1) mod 11 == 0
    X represents the value 10.
    
    :param isbn: str - ISBN string (with or without hyphens).
    :return: bool - True if valid ISBN-10, False otherwise.
    
    Examples:
    >>> is_valid("3-598-21508-8")
    True
    >>> is_valid("3-598-21507-X")
    True
    >>> is_valid("3-598-21508-9")
    False
    >>> is_valid("3598215088")
    True
    """
    # Remove hyphens from the ISBN
    cleaned = isbn.replace("-", "")
    
    # ISBN-10 must have exactly 10 characters
    if len(cleaned) != 10:
        return False
    
    # Check that first 9 characters are digits
    if not cleaned[:9].isdigit():
        return False
    
    # Last character must be digit or 'X'
    if not (cleaned[9].isdigit() or cleaned[9] == 'X'):
        return False
    
    # Calculate the weighted sum
    total = 0
    for i, char in enumerate(cleaned):
        weight = 10 - i  # Weights go from 10 down to 1
        
        if char == 'X':
            # X represents 10, only valid as last character
            if i != 9:
                return False
            value = 10
        else:
            value = int(char)
        
        total += value * weight
    
    # Valid if sum is divisible by 11
    return total % 11 == 0