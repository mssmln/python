# Sum All Numbers in a Range
# 
# We'll pass you an array of two numbers. 
# Return the sum of those two numbers plus the sum of all the numbers between them. 
# The lowest number will not always come first.
# For example, sumAll([4,1]) should return 10 because sum of all 
# the numbers between 1 and 4 (both inclusive) is 10.


def sumAll (arr) :
    n = 0
    i = min(arr)
    while i <= max(arr) :
        n = n + i
        i = i + 1
    return n


print(sumAll([1, 4])) 