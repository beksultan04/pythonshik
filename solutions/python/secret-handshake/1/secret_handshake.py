def commands(binary_str):
    """
    Convert a binary string (representing a number) into the secret handshake actions.

    - Considers only the rightmost 5 bits (pads left with zeros if needed).
    - Bit positions (from rightmost):
        0 -> wink
        1 -> double blink
        2 -> close your eyes
        3 -> jump
        4 -> reverse the order of the operations
    - Returns a list of action strings.
    """
    if not isinstance(binary_str, str):
        raise TypeError("binary_str must be a string")

    if any(ch not in "01" for ch in binary_str):
        raise ValueError("binary_str must contain only '0' and '1' characters")

    # Ensure we have exactly the rightmost 5 bits (pad on the left with zeros if needed)
    bits = binary_str.zfill(5)[-5:]

    actions_map = [
        "wink",
        "double blink",
        "close your eyes",
        "jump"
    ]

    result = []
    # Check bits from rightmost (index 4) to index 1 (for the 4 action bits)
    for i in range(4):  # i=0 -> rightmost action bit, i=3 -> fourth bit from right
        bit = bits[-1 - i]
        if bit == "1":
            result.append(actions_map[i])

    # If the 5th bit from the right (bits[0]) is set, reverse the actions
    if bits[0] == "1":
        result.reverse()

    return result
