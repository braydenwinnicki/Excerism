def sum_of_multiples(limit, multiples):
    valid_multiples = {num for base in multiples if base > 0 for num in range(base, limit, base)}
    return sum(valid_multiples)
    
