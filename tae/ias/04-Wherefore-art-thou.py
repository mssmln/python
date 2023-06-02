# Wherefore art thou
# 
# Make a function that looks through an array of objects (first argument) and 
# returns an array of all objects that have matching name and value pairs (second argument). 
# Each name and value pair of the source object has to be present in the 
# object from the collection if it is to be included in the returned array.


def whatIsInAName (collection, source) :
    l = list()
    i = 0
    copy = collection.copy()
    k = list(source.keys())
    
    while i < len(collection) :
        obj = copy.pop(0)
        k_in_obj_and_same_value = [el in obj and source[el] is obj[el] for el in k]
        if all(k_in_obj_and_same_value) :
            l.append(obj)
        i += 1
    return l


print(whatIsInAName([
    { "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }], 
    { "apple": 1, "cookie": 2 }))