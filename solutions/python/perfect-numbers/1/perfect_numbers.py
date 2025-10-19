def classify(number):
    """Classify a number as perfect, abundant, or deficient.
    
    Classification based on aliquot sum (sum of proper divisors):
    - Perfect: number equals its aliquot sum
    - Abundant: number is less than its aliquot sum
    - Deficient: number is greater than its aliquot sum
    
    :param number: int - a positive integer to classify.
    :return: str - "perfect", "abundant", or "deficient".
    :raises ValueError: if number is not a positive integer.
    
    Examples:
    >>> classify(6)
    'perfect'
    >>> classify(12)
    'abundant'
    >>> classify(8)
    'deficient'
    """
    # Validate input - must be a positive integer
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    # Calculate aliquot sum (sum of proper divisors, excluding the number itself)
    aliquot_sum = 0
    
    # Find all divisors from 1 to number/2
    # (no divisor greater than number/2 except the number itself)
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            aliquot_sum += i
    
    # Classify based on comparison with aliquot sum
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"