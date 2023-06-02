# Diff Two Arrays
# 
# Compare two arrays and return a new array with any items only found 
# in one of the two given arrays, but not both. In other words, 
# return the symmetric difference of the two arrays.
# Note: You can return the array with its elements in any order.


def diffArray (arr1, arr2) :
    return list(filter(lambda el: el not in arr1 or el not in arr2, arr1 + arr2))


print(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]))