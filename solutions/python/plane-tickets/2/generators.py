"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""

    sequence = ["A", "B", "C", "D"]

    for number in range(number):
        yield sequence[number % 4]
              
def generate_seats(number):
    """Generate a series of identifiers for airline seats."""

    letter_generator = generate_seat_letters(number)
    letters = []
    for _ in range(number):
        let = next(letter_generator, None)
        letters.append(let)
    
    numbers = []

    for seat in range(number + 1):
        if seat not in (0, 13):
            for _ in range(4):
                numbers.append(seat)

    codes = zip(letters, numbers)
    
    for letter, row in codes:
        yield f"{row}{letter}"

def assign_seats(passengers):
    """Assign seats to passengers."""

    manifest = {}

    seat_generator = generate_seats(len(passengers))
    
    for person in passengers:
        seat_code = next(seat_generator, None)
        manifest[person] = seat_code

    return manifest

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket."""

    for seat in seat_numbers:
        code = seat + flight_id
        full_code = code + "0" * (12 - len(code))
        yield full_code