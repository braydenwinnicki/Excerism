def find(search_list, value):
    left = 0
    right = len(search_list) - 1

    while left <= right:
        # Find the middle index between our current left and right boundaries
        middle = (left + right) // 2
        
        if search_list[middle] == value:
            return middle  # Found it! Returns the correct original index.
        
        elif search_list[middle] > value:
            # The value is smaller, so ignore the right half
            right = middle - 1
        else:
            # The value is larger, so ignore the left half
            left = middle + 1

    # If the loop finishes without returning, the value isn't there
    raise ValueError("value not in array")
            

        
    
        