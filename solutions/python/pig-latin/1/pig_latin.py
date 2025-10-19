def translate(text):
    """
    Translate `text` (one or more words) into Pig Latin.
    """
    vowels = set("aeiou")

    def translate_word(word):
        if not word:
            return word

        w = word.lower()  # exercise examples use lowercase; if needed preserve case, adjust here

        # Rule 1: starts with vowel or "xr" or "yt"
        if w[0] in vowels or w.startswith("xr") or w.startswith("yt"):
            return w + "ay"

        # Otherwise find the index where "vowel" occurs.
        # 'y' acts as a vowel when it is not at position 0.
        i = 0
        while i < len(w):
            ch = w[i]
            # treat 'qu' as part of consonant cluster
            if ch == "q" and i + 1 < len(w) and w[i + 1] == "u":
                i += 2
                continue
            # vowel found
            if ch in vowels or (ch == "y" and i != 0):
                break
            i += 1

        return w[i:] + w[:i] + "ay"

    return " ".join(translate_word(word) for word in text.split())
