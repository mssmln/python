# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


def problem11 (string, arr) :
    # condition to append to the all method
    are_all_str = [type(w) is str for w in arr]

    if type(string) is str and all(are_all_str) :
        # to enable regex
        import re
        # search is like js' test method
        return list(filter(lambda el: re.search(f'^{string}', el), arr))
    else : 
        return 'all the args are to be string'


print(problem11('de', ['dog', 'ddeer', 'deal']))