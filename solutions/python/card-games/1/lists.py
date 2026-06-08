"""Functions for tracking poker hands and assorted card tasks."""



def get_rounds(number):
    """Create a list containing the current and next two round         numbers."""
    
    second_number = number + 1
    third_number = number + 2
    
    return [number, second_number, third_number]

def concatenate_rounds(rounds_1, rounds_2):
    """concatenate"""

    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""

    return number in rounds

def card_average(hand):
    """Calculate and returns the average card value from the            list."""

    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR         ('middle' card) == calculated average."""

    avg = card_average(hand)
    n = len(hand)
    
    median = hand[ n // 2]
        
    new_avg = (hand[0] + hand[-1]) / 2 

    if new_avg == avg or median == avg:
        return True
    return False

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) ==          (average of odd indexed card values)."""

    even = []
    odd = []


    for index, card in enumerate(hand):
        if index % 2 == 0:
            even.append(card)

        odd.append(card)

    if sum(even) / len(even) == sum(odd) / len(odd):
        return True
    return False

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2."""
    
    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand