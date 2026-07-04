def square_of_sum(number):
    list = []
    for n in range(1, (number + 1)):
        list.append(n)
    return sum(list) ** 2
        


def sum_of_squares(number):
    list = []
    total = 0
    for n in range(1, (number + 1)):
        list.append(n)
    for n in list:
        total += (n ** 2)
    return total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
