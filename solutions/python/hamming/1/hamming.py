def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    distance = 0

    for index, letter in enumerate(strand_a):
        if letter != strand_b[index]:
            distance += 1

    return distance 
            
