def score(x, y):
    """Calculate the points scored in a single dart toss.
    
    Scoring zones (concentric circles centered at origin):
    - Inner circle (radius ≤ 1): 10 points
    - Middle circle (radius ≤ 5): 5 points
    - Outer circle (radius ≤ 10): 1 point
    - Outside target (radius > 10): 0 points
    
    :param x: float - x coordinate of dart landing position.
    :param y: float - y coordinate of dart landing position.
    :return: int - points scored.
    
    Examples:
    >>> score(0, 0)
    10
    >>> score(0, 5)
    5
    >>> score(0, 10)
    1
    >>> score(0, 11)
    0
    >>> score(3, 4)
    5
    """
    # Calculate distance from center using Pythagorean theorem
    # Distance = sqrt(x² + y²)
    distance = (x ** 2 + y ** 2) ** 0.5
    
    # Determine score based on which circle the dart landed in
    if distance <= 1:
        return 10  # Inner circle
    elif distance <= 5:
        return 5   # Middle circle
    elif distance <= 10:
        return 1   # Outer circle
    else:
        return 0   # Outside target