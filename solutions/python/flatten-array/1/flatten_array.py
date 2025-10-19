from collections.abc import Iterable

def flatten(iterable):
    """
    Take a nested iterable of any depth and return a flat list.
    Excludes None values. Strings/bytes/bytearray are treated as atomic.
    """
    result = []
    for item in iterable:
        if item is None:
            # skip null-like values
            continue
        # treat strings/bytes/bytearray as non-iterable for flattening purposes
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes, bytearray)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
