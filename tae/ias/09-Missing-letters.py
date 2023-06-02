# Missing letters
# 
# Find the missing letter in the passed letter range and return it.
# If all letters are present in the range, return undefined.

    
def fearNotLetter(string):
    i = 1
    while i < len(string):
        # ord is like js' charCodeAt()
        if ord(string[i]) - ord(string[i - 1]) > 1:
            # chr is like js' fromCharCode()
            return chr(ord(string[i - 1]) + 1)
        i += 1


print(fearNotLetter("stvwx"))