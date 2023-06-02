# Arguments Optional
# 
# Create a function that sums two arguments together. If only one argument is provided, then return a function that expects one argument and returns the sum.
# For example, addTogether(2, 3) should return 5, and addTogether(2) should return a function.
# Calling this returned function with a single argument will then return the sum:
# var sumTwoAnd = addTogether(2);
# sumTwoAnd(3) returns 5.
# If either argument isn't a valid number, return undefined.


def addTogether (*args) :
    def valid_num (num) : 
        import numbers
        return isinstance(num, numbers.Number)
    
    if len(args) == 2 and valid_num(args[0]) and valid_num(args[1]) :
        return args[0] + args[1]
    elif len(args) == 1 and valid_num(args[0]) :
        return lambda x: x + args[0] if valid_num(x) else None
    else : return None


print(addTogether(23, 30))
print(addTogether(5)(7))
print(addTogether("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
print(addTogether(2)([3]))