# Smallest Common Multiple
# 
# Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.
# The range will be an array of two numbers that will not necessarily be in numerical order.
# For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.


def smallestCommons (arr) :
    MAX = max(arr)
    MIN = min(arr)
    range = []
    i = MIN
    while i < MAX + 1 :
        range.append(i)
        i += 1
    
    counter = 2
    ind = 1
    while ind < counter :
        if MAX * ind % MIN == 0 :
            boo = [(MAX * ind / el).is_integer() for el in range]
            if all(boo) :
                r = MAX * ind
            else : counter += 1
        else : counter += 1
        ind += 1
    return r


print(smallestCommons([23, 18]))