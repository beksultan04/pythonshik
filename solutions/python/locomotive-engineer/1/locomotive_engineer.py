"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.
    
    :param wagons: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.
    
    Move first two wagons to the end, insert missing wagons after locomotive (ID=1).
    
    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    
    Example:
    >>> fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
    [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]
    """
    # Unpack: first two wagons, locomotive, and the rest
    first, second, locomotive, *rest = each_wagons_id
    
    # Reorder: locomotive, missing wagons, rest, then first two at the end
    return [locomotive, *missing_wagons, *rest, first, second]


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.
    
    :param route: dict - the dict of routing information.
    :param stops: arbitrary number of stops as keyword arguments.
    :return: dict - updated route dictionary.
    """
    # Extract stop values and add them to route
    return {**route, "stops": list(stops.values())}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.
    
    :param route: dict - the route information.
    :param more_route_information: dict - extra route information.
    :return: dict - extended route information.
    """
    # Merge both dictionaries using unpacking
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.
    
    Transpose the wagon grid so columns align by color.
    
    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    
    Example:
    >>> fix_wagon_depot([
    ...     [(2, "red"), (4, "red"), (8, "red")],
    ...     [(5, "blue"), (9, "blue"), (13, "blue")],
    ...     [(3, "orange"), (7, "orange"), (11, "orange")]
    ... ])
    [[(2, "red"), (5, "blue"), (3, "orange")],
     [(4, "red"), (9, "blue"), (7, "orange")],
     [(8, "red"), (13, "blue"), (11, "orange")]]
    """
    # Unpack rows and transpose using zip
    row1, row2, row3 = wagons_rows
    return [list(column) for column in zip(row1, row2, row3)]