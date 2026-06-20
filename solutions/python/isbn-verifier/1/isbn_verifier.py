def is_valid(isbn):
    isbn = list(isbn.replace("-", ""))
    if len(isbn) != 10:
        return False
    
    if isbn[-1].isalpha():
        if isbn[-1] == "X" or isbn[-1] == "x":
            isbn[-1] = "10"
        else:
            return False 

        
    isbn_ints = []
    for number in isbn:
        if number.isdigit():
            isbn_ints.append(int(number))
        else:
            return False  

    d1, d2, d3, d4, d5, d6, d7, d8, d9, dc = isbn_ints

    
    if (d1 * 10 + d2 * 9 + d3 * 8 + d4 * 7 + d5 * 6 + d6 * 5 + d7 * 4 + d8 * 3 + d9 * 2 + dc * 1) % 11 == 0:
        return True

    return False