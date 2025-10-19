def square_root(number):
    """
    Return the integer square root of `number` when it's a perfect square.
    Uses binary search; raises ValueError if `number` is not a perfect square.
    """
    if number < 0:
        raise ValueError("number must be non-negative")
    if number in (0, 1):
        return number

    low, high = 1, number // 2
    while low <= high:
        mid = (low + high) // 2
        sq = mid * mid
        if sq == number:
            return mid
        if sq < number:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("input is not a perfect square")
