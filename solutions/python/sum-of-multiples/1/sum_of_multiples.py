def sum_of_multiples(limit, multiples):
    """
    Return the sum of all unique multiples of the given factors that are less than `limit`.
    Zero factors are ignored (multiples of 0 are undefined).
    """
    if limit <= 0 or not multiples:
        return 0

    uniques = set()
    for factor in multiples:
        if factor <= 0:
            continue
        # add every multiple of factor less than limit
        for n in range(factor, limit, factor):
            uniques.add(n)

    return sum(uniques)
