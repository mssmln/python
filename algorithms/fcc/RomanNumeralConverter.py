# Convert the given number into a roman numeral.
# All roman numerals answers should be provided in upper-case.


def convertToRoman(num) :
    rn = dict(
        M = 1000,
        CM = 900,
        D = 500,
        CD = 400,
        C = 100,
        XC = 90,
        L = 50,
        XL = 40,
        X = 10,
        IX = 9,
        V = 5,
        IV = 4,
        I = 1
    )

    r = 0
    rr = ''
    a = list()
    ar = list()
    
    for rom in rn :
        if num >= rn[rom] :
            a.append(rn[rom])
            ar.append(rom)

    i = 0
    for el in a :
        while r < num :
            r += el
            rr += ar[i]
            if r > num :
                import re
                r -= el
                # rf because i needed to use both a regex and a dynamic value
                # i tried out with replace method but didn't work
                rr = re.sub(rf'{ar[i]}$', '', rr)
                i += 1 
                break
    return rr


print(convertToRoman(10000000000))