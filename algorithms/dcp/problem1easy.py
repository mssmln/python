# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


def problem1(arr, k) :
    for it in arr :
        for el in arr[slice(1, len(arr))] :
            r = 0
            if (arr.index(el) > arr.index(it)) :
                r = it + el
            if (r == k) :
                print(f'true because {it} + {el}')


problem1([3, 5, 2, 15, 9, 8, 14], 17)