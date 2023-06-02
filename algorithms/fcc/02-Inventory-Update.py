# Inventory Update
# Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. Update the current existing inventory item quantities (in arr1). If an item cannot be found, add the new item and quantity into the inventory array. The returned inventory array should be in alphabetical order by item.


def updateInventory(arr1, arr2) :
    falsy = []
    for el in arr2 :
        for en in arr1 :
            # couldn't use this sol because couldn't access en
            # if any(en[1] == el[1] for en in arr1) :
            if en[1] == el[1] :
                en[0] += el[0]
                continue
            else :
                falsy.append(False)

        if len(falsy) == len(arr1) :
            arr1.append(el)
        falsy.clear()
    
    arr1.sort(key=lambda x: x[1])            
    return arr1


print(updateInventory(
    [[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], 
    [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]))


print(updateInventory(
    [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], 
    [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]))