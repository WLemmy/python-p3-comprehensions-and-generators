#!/usr/bin/env python3
def return_evens(num_list):
    # Termination condition: if the list is empty, return an empty list
    if not num_list:
        return []
    
    # Check if the first element of the list is even
    if num_list[0] % 2 == 0:
        # If it's even, include it in the result and recursively call return_evens
        # on the rest of the list
        return [num_list[0]] + return_evens(num_list[1:])
    else:
        # If it's odd, just recursively call return_evens on the rest of the list
        return return_evens(num_list[1:])

# Test the function
print(return_evens([0, 1, 3, 5, 7, 8, 9]))
