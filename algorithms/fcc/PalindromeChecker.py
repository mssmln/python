# Return true if the given string is a palindrome. Otherwise, return false.
# A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.
# Note: You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn everything into the same case (lower or upper case) in order to check for palindromes.
# We'll pass strings with varying formats, such as racecar, RaceCar, and race CAR among others.
# We'll also pass strings with special symbols, such as 2A3*3a2, 2A3 3a2, and 2_A3*3#A2.


def palindrome(string) :
    import re
    s = re.findall(r'[a-z0-9]', string.lower())
    inc = 1
    for l in s :
        inc += 1 if l == s[len(s) - inc] else False
    return inc - 1 == len(s)


print(palindrome("eye")) 
print(palindrome("_eye")) 
print(palindrome("race car")) 
print(palindrome("not a palindrome"))
print(palindrome("A man, a plan, a canal. Panama")) 
print(palindrome("never odd or even")) 
print(palindrome("nope")) 
print(palindrome("almostomla")) 
print(palindrome("My age is 0, 0 si ega ym.")) 
print(palindrome("1 eye for of 1 eye.")) 
print(palindrome("0_0 (: /-\ :) 0-0")) 
print(palindrome("five|\_/|four"))