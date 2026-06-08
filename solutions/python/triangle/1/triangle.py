def equilateral(sides):

    a, b, c = sides

    if check_triangle(sides):
    
        if a == b and a == c and b == c:
            return True
    return False

def isosceles(sides):
  
    a, b, c = sides
    
    if check_triangle(sides):
        if a == b or a == c or c == b:
            return True
    return False 


def scalene(sides):

    a, b, c = sides

    if check_triangle(sides):

        if a != b and a != c and b != c:
            return True 
    return False 

def check_triangle(sides):
    a, b, c = sides

    if 0 in sides:
        return False
    
    if a + b >= c and b + c >= a and a + c >= b:
        return True
    return False

