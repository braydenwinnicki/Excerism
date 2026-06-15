def classify(number):
    """ A perfect number equals the sum of its positive divisors."""

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.") 

    
    factors = []

    for n in range(1, int((number ** .5)) + 1 ):
        if number % n == 0:
            factors.append(n)
            factors.append(int(number / n))

    factors = set(factors)
    factors.remove(number)

    if sum(factors) == number:
        return "perfect"
    if sum(factors) < number:
        return "deficient"
    if sum(factors) > number:
        return "abundant"
    return None

        
