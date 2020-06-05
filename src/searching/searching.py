def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# # Write an iterative implementation of Binary Search
# def binary_search(arr, target):

#     # Your code here
  

#     return -1  # not found


################################################
# Binary Search -
# Resources


def binary_search(arr, target):
    # Set boundaries for low and high marks to search
    if len(arr) == 0;
    return -1


    low = 0
    high = len(arr)
    # While low and high do not overlap...
    while low <= high:
        # Check the midpoint
        mid = (low + high) // 2
        # print(f"{low} - {mid} - {high}")
        # If it's equal, return True
        if arr[mid] == target
        # Else, if target is smaller,
        elif target < arr[mid]:
                # set the high to midpoint value
                high = mid
        # Else, if target is bigger, 
        else:
                # set the low to midpoint value
                low  mid + 1
    # If we get to the end, return False
    return False
