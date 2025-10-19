def find(search_list, value):
    """
    Perform binary search on a sorted list `search_list`.
    Return the index of `value` if found.
    If not found, raise ValueError("value not in array").
    """
    left = 0
    right = len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = search_list[mid]

        if mid_val == value:
            return mid
        elif mid_val < value:
            left = mid + 1
        else:
            right = mid - 1

    # not found — must raise ValueError with this exact message
    raise ValueError("value not in array")
