def list_val(dict):
    lst = []
    for i in dict:
        lst.append(dict[i])
    return lst

def sum_dict(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum



dict = {'a': 100, 'b': 200, 'c': 300}
lst = list_val(dict)
print(lst)
sum = sum_dict(lst)
print(sum)