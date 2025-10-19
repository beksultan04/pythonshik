def transform(legacy_data):
    """
    Convert legacy mapping {score: [LETTERS...], ...}
    to {letter: score, ...} with letters in lowercase.
    """
    result = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            result[letter.lower()] = score
    return result
