# Input:
# original_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)
#
# Output:  {'c':3, 'a':1, 'b':2}

dict = {'a': 1, "b": 2}
print("Original dictionary is: ", dict)
item = ('c', 3)
item = list(item)
item_dict = dict.fromkeys(item[0], item[1])
print("Dictionary made from puple item: ", item_dict)
concantinated_dicts = item_dict | dict
print("Concantinated: ", concantinated_dicts)