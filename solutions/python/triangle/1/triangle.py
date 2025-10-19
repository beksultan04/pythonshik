def equilateral(sides):
    """Determine if a triangle is equilateral.
    
    An equilateral triangle has all three sides the same length.
    
    :param sides: list[float] - three side lengths.
    :return: bool - True if equilateral, False otherwise.
    
    Examples:
    >>> equilateral([2, 2, 2])
    True
    >>> equilateral([2, 3, 2])
    False
    """
    # Check if it's a valid triangle first
    if not is_valid_triangle(sides):
        return False
    
    # All three sides must be equal
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """Determine if a triangle is isosceles.
    
    An isosceles triangle has at least two sides the same length.
    
    :param sides: list[float] - three side lengths.
    :return: bool - True if isosceles, False otherwise.
    
    Examples:
    >>> isosceles([3, 4, 4])
    True
    >>> isosceles([3, 3, 3])
    True
    >>> isosceles([3, 4, 5])
    False
    """
    # Check if it's a valid triangle first
    if not is_valid_triangle(sides):
        return False
    
    # At least two sides must be equal
    a, b, c = sides
    return a == b or b == c or a == c


def scalene(sides):
    """Determine if a triangle is scalene.
    
    A scalene triangle has all sides of different lengths.
    
    :param sides: list[float] - three side lengths.
    :return: bool - True if scalene, False otherwise.
    
    Examples:
    >>> scalene([3, 4, 5])
    True
    >>> scalene([3, 3, 4])
    False
    """
    # Check if it's a valid triangle first
    if not is_valid_triangle(sides):
        return False
    
    # All three sides must be different
    a, b, c = sides
    return a != b and b != c and a != c


def is_valid_triangle(sides):
    """Check if three sides can form a valid triangle.
    
    Rules:
    - All sides must be > 0
    - Sum of any two sides must be >= the third side (triangle inequality)
    
    :param sides: list[float] - three side lengths.
    :return: bool - True if valid triangle, False otherwise.
    """
    a, b, c = sides
    
    # All sides must be positive
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Triangle inequality: sum of any two sides >= third side
    if a + b < c or b + c < a or a + c < b:
        return False
    
    return True