# Seek and Destroy
# 
# You will be provided with an initial array (the first argument in the destroyer function), 
# followed by one or more arguments. Remove all elements from the initial array 
# that are of the same value as these arguments.
# Note: You have to use the arguments object.


def destroyer (arr, *args) :
    return list(filter(lambda el: el not in args, arr))


print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))