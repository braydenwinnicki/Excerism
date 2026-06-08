"""This module calculates baking and preparation times for lasagna."""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining"""

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layer):
    """ calculate time for prep based on number of layers"""

    return number_of_layer * PREPARATION_TIME
    
def elapsed_time_in_minutes(number_of_layer, elapsed_baking_time):
    """calculate total elapsed time in minutes"""

    return preparation_time_in_minutes(number_of_layer) + elapsed_baking_time