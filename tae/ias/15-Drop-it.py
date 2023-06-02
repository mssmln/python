# Drop it
# 
# Given the array arr, iterate through and remove each element starting from the first element (the 0 index) until 
# the function func returns true when the iterated element is passed through it.
# Then return the rest of the array once the condition is satisfied, otherwise, arr should be returned as an empty array.


def dropElements (arr, func) :
    for el in arr :
        if func(el) :
            f_o = el
            break
    if (i := arr.index(f_o)) == -1 : return []
    else : return arr[i:]


print(dropElements([1, 2, 3, 9, 2], lambda n : n > 2))