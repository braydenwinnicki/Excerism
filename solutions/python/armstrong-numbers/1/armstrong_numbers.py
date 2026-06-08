def is_armstrong_number(number):
    
    total = 0
    str_number = str(number)

    for digit in str_number:
        digit_value = int(digit) ** len(str_number)
        total += digit_value 

    return total == number
        
        
        
    
