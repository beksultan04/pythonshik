def leap_year(year):
    """Determine whether a given year is a leap year.
    
    A leap year occurs:
    - Every year divisible by 4
    - EXCEPT years divisible by 100
    - UNLESS also divisible by 400
    
    :param year: int - year to check.
    :return: bool - True if leap year, False otherwise.
    
    Examples:
    >>> leap_year(2000)
    True
    >>> leap_year(1900)
    False
    >>> leap_year(2020)
    True
    >>> leap_year(1997)
    False
    """
    # Divisible by 400 -> leap year
    if year % 400 == 0:
        return True
    
    # Divisible by 100 (but not 400) -> NOT a leap year
    if year % 100 == 0:
        return False
    
    # Divisible by 4 (but not 100) -> leap year
    if year % 4 == 0:
        return True
    
    # Not divisible by 4 -> NOT a leap year
    return False