# Convert HTML Entities
# Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a string to their corresponding HTML entities.


def convertHTML (string) :
    obj = {
        "&" : "&amp;",
        "<" : "&lt;",
        ">" : "&gt;",
        '"' : "&quot;",
        "'" : "&apos;"
    }
    newStr = ''
    for char in list(string) :
        if char in obj :
            newStr += obj[char]
        else : newStr += char
    return newStr


print(convertHTML("<>"))