def append(list1, list2):
    return list1 + list2


def concat(lists):
    new_list = []
    for item in lists:
        if isinstance(item, list):
            new_list = new_list + item 
    return new_list
            


def filter(function, list):
    return [item for item in list if function(item) == True]


def length(list):
    count = 0
    for item in list:
        count += 1
    return count


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator
    
    

def foldr(function, list, initial):
    list = list[::-1]
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator
    


def reverse(list):
    return list[::-1]
