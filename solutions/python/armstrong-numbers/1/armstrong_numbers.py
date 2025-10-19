def is_armstrong_number(number):
    """Determine if a number is an Armstrong number.
    
    An Armstrong number is a number that equals the sum of its own 
    digits each raised to the power of the number of digits.
    
    :param number: int - number to check.
    :return: bool - True if Armstrong number, False otherwise.
    
    Examples:
    >>> is_armstrong_number(9)
    True
    >>> is_armstrong_number(10)
    False
    >>> is_armstrong_number(153)
    True
    >>> is_armstrong_number(154)
    False
    """
    # Convert number to string to get digits
    digits_str = str(number)
    
    # Count number of digits
    num_digits = len(digits_str)
    
    # Calculate sum of each digit raised to power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits_str)
    
    # Check if sum equals original number
    return sum_of_powers == number