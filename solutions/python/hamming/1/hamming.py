def distance(strand_a, strand_b):
    """
    Return the Hamming distance between two DNA strands.
    Raises ValueError("Strands must be of equal length.") if lengths differ.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(1 for a, b in zip(strand_a, strand_b) if a != b)
