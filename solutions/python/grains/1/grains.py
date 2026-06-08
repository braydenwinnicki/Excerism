def square(number):
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    exponent = number - 1

    return 1 * (2 ** exponent)

def total():

    total = []

    for number in range(1, 65):
        total.append(square(number))

    return sum(total)
        
