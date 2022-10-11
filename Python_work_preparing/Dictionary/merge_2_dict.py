def merge(dict1, dict2):
    dict1.update(dict2)
    return dict1

# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict_new = merge(dict1, dict2)
print(dict_new)