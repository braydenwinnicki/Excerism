def flatten(iterable):

    new_array = []
    
    for item in iterable:
        if isinstance(item, list):
            new_array.extend(flatten(item))
        if isinstance(item, int):
            new_array.append(item)
       
            

    return new_array
            
