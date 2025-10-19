def find_anagrams(word, candidates):
    """
    Return a list of candidates that are anagrams of `word`.

    - Comparison is case-insensitive.
    - A candidate that is the same word (ignoring case) is NOT considered an anagram.
    - The returned list preserves the order and original casing of candidates.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    target = word.lower()
    # canonical form: sorted characters in lowercase
    target_sorted = sorted(target)

    result = []
    for cand in candidates:
        if not isinstance(cand, str):
            continue
        cand_lower = cand.lower()
        if cand_lower == target:
            # identical word (case-insensitive) — not an anagram
            continue
        if sorted(cand_lower) == target_sorted:
            result.append(cand)
    return result
