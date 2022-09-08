def steamrollArray(arr) :
    a = list()
    for el in arr :
        if type(el) is list :
            # in js i used ... and push over +=
            a += steamrollArray(el)
        else :
            a.append(el)
    return a

  
print(steamrollArray([1, [2], [3, [[4]]]]))