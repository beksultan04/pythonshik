def is_paired(input_string):
    """
    Return True if all brackets in input_string are correctly paired and nested.
    Brackets considered: (), [], {}. All other characters are ignored.
    """
    pairs = {')': '(', ']': '[', '}': '{'}
    opens = set(pairs.values())
    stack = []

    for ch in input_string:
        if ch in opens:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return not stack
