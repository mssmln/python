# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.


def problem4 (arr) :
    sort_pos_uni_num = set(filter(lambda el: el > -1, arr))
    for val in list(sort_pos_uni_num) :
        if not val + 1 in list(sort_pos_uni_num) :
            return val + 1
    

print(problem4([3, 4, -1, 1, 1]))
print(problem4([1, 2, 0]))