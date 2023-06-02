# Everything Be True
# 
# Check if the predicate (second argument) is truthy on all elements of a collection (first argument).
# In other words, you are given an array collection of objects. 
# The predicate pre will be an object property and you need to return true if its value is truthy. 
# Otherwise, return false.
# In JavaScript, truthy values are values that translate to true when evaluated in a Boolean context.
# Remember, you can access object properties through either dot notation or [] notation.


def truthCheck (collection, pre) :
    pre_in_coll = [pre in el and el[pre] for el in collection]
    return all(pre_in_coll)


print(truthCheck([
    {"name": "Quincy", "role": "Founder", "isBot": False}, 
    {"name": "Naomi", "role": "", "isBot": False}, 
    {"name": "Camperbot", "role": "Bot", "isBot": True}], 
    "isBot"))


print(truthCheck([
    {"id": 1, "data": {"url": "https://freecodecamp.org", "name": "freeCodeCamp"}}, 
    {"id": 2, "data": {"url": "https://coderadio.freecodecamp.org/", "name": "CodeRadio"}}, 
    {"id": None, "data": {}}], 
    "data"))


print(truthCheck([
    {"name": "freeCodeCamp", "users": [{"name": "Quincy"}, 
    {"name": "Naomi"}]}, 
    {"name": "Code Radio", "users": [{"name": "Camperbot"}]}, 
    {"name": "", "users": []}], 
    "users"))


print(truthCheck([
    {"id": 1, "data": {"url": "https://freecodecamp.org", "name": "freeCodeCamp"}}, 
    {"id": 2, "data": {"url": "https://coderadio.freecodecamp.org/", "name": "CodeRadio"}}, 
    {"id": 3, "data": {}}], 
    "id"))