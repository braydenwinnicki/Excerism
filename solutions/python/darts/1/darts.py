def score(x, y):

    slope = (((0 - x) ** 2) + ((0 - y ) ** 2)) ** .5 

    if slope <= 1:
        return 10  # Inner circle
    if slope <= 5:
        return 5   # Middle circle
    if slope <= 10:
        return 1   # Outer circle
    return 0   # Outside the target