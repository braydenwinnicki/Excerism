"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers."""

    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons."""

    a, b, loco, *rest = each_wagons_id

    new_list = [loco, *missing_wagons, *rest, a, b]

    return new_list

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict."""
    
    stop_list = dict(kwargs)
    stops = []
    for stop in stop_list.values():
        stops.append(stop)
    
        
    full_route = {"from" : route["from"], "to": route["to"], "stops": stops}
    return full_route

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information."""

    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons."""

    grid = []
    for row in zip(*wagons_rows):
        grid.append(list(row))

    return grid