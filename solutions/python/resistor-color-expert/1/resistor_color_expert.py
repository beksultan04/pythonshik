def resistor_label(colors):
    """
    Translate resistor color bands to a human-readable label.

    Supported lengths:
      - 1 band (only 'black' expected) -> "0 ohms"
      - 4 bands -> value from 2 digits + multiplier, tolerance is 4th band
      - 5 bands -> value from 3 digits + multiplier, tolerance is 5th band

    Returns strings like:
      "33 ohms ±0.5%"
      "33 kiloohms ±0.05%"
      "33 megaohms ±2%"
    """
    # maps for digit and tolerance values
    digit = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    tolerance = {
        "grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
        "brown": 1.0, "red": 2.0, "gold": 5.0, "silver": 10.0
    }

    if not isinstance(colors, (list, tuple)):
        raise TypeError("colors must be a list or tuple of color names")

    # normalize to lower-case strings
    cols = [c.lower() for c in colors]

    n = len(cols)
    if n == 0:
        raise ValueError("no color bands provided")

    # One-band resistor (spec says only black with value 0)
    if n == 1:
        if cols[0] != "black":
            # spec: one-band resistors only black, but handle gracefully
            if cols[0] in digit:
                value = digit[cols[0]]
                return f"{value} ohms"
            raise ValueError("unsupported single-band color")
        return "0 ohms"

    # Build main value and tolerance for 4- and 5-band variants
    if n == 4:
        # v1, v2, multiplier, tolerance
        if cols[0] not in digit or cols[1] not in digit or cols[2] not in digit:
            raise ValueError("invalid color for digit/multiplier")
        v1 = digit[cols[0]]
        v2 = digit[cols[1]]
        mult = digit[cols[2]]
        main_value = (v1 * 10 + v2) * (10 ** mult)
        tol_color = cols[3]
    elif n == 5:
        # v1, v2, v3, multiplier, tolerance
        if cols[0] not in digit or cols[1] not in digit or cols[2] not in digit or cols[3] not in digit:
            raise ValueError("invalid color for digit/multiplier")
        v1 = digit[cols[0]]
        v2 = digit[cols[1]]
        v3 = digit[cols[2]]
        mult = digit[cols[3]]
        main_value = (v1 * 100 + v2 * 10 + v3) * (10 ** mult)
        tol_color = cols[4]
    else:
        raise ValueError("unsupported number of bands (supported: 1, 4, 5)")

    if tol_color not in tolerance:
        raise ValueError("invalid tolerance color")

    tol_val = tolerance[tol_color]

    # Format main value into ohms/kiloohms/megaohms with tidy representation
    if main_value >= 1_000_000:
        display_value = main_value / 1_000_000
        unit = "megaohms"
    elif main_value >= 1_000:
        display_value = main_value / 1_000
        unit = "kiloohms"
    else:
        display_value = main_value
        unit = "ohms"

    # Remove unnecessary .0 for integer values; keep decimal if needed
    if isinstance(display_value, float) and display_value.is_integer():
        display_str = str(int(display_value))
    else:
        # use general format to avoid trailing zeros
        display_str = "{:g}".format(display_value)

    # Format tolerance similarly (avoid trailing zeros)
    tol_str = "{:g}".format(tol_val)

    return f"{display_str} {unit} ±{tol_str}%"
