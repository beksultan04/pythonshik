def steps(number):
    """Calculate the number of steps to reach 1 using Collatz Conjecture rules.
    
    Rules:
    - If the number is even: divide by 2
    - If the number is odd: multiply by 3 and add 1
    - Repeat until reaching 1
    
    :param number: int - positive integer to start from.
    :return: int - number of steps to reach 1.
    :raises ValueError: if number is not a positive integer.
    
    Examples:
    >>> steps(1)
    0
    >>> steps(12)
    9
    >>> steps(16)
    4
    >>> steps(1000000)
    152
    """
    # Validate input - must be a positive integer
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    # If already at 1, no steps needed
    if number == 1:
        return 0
    
    # Count steps
    step_count = 0
    current = number
    
    while current != 1:
        if current % 2 == 0:
            # Even: divide by 2
            current = current // 2
        else:
            # Odd: multiply by 3 and add 1
            current = current * 3 + 1
        
        step_count += 1
    
    return step_count