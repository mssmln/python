# One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift cipher. In a shift cipher the meanings of the letters are shifted by some set amount.
# A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places. Thus A ↔ N, B ↔ O and so on.
# Write a function which takes a ROT13 encoded string as input and returns a decoded string.
# All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation), but do pass them on.


def rot13(string) :
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
    r = ''
    for lett in list(string) :
        try :
            ind = alp.index(lett) + 13
            r += alp[ind]
        except :
            r += lett
    return r

  
print(rot13("SERR PBQR PNZC"))
print(rot13("SERR CVMMN!"))
print(rot13("SERR YBIR?"))
print(rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT."))