# example:
# The original dictionary:  {‘gfg’: [5, 6, 7, 8], ‘best’: [6, 12, 10, 8], ‘is’: [10, 11, 7, 5], ‘for’: [1, 2, 5]}
# The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]

# driver code:
dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

print("Original dict: ", dict)

lst = list(dict.values())
print(lst)
simple_lst = []
i = 0
e = 0

while(i < len(lst)):
    e = 0
    while(e < len(lst[i])):
        simple_lst.append(lst[i][e])
        e += 1
    i += 1

# for elem in lst:
#     for el in elem:
#         simple_lst.append(el)
print("full simple list: ", simple_lst)

def is_uniq(uniq, n):
    res = True
    i = 0
    while(i < len(uniq)):
        if(uniq[i] == n):
            res = False
        i += 1
    return res
i = 0
e = 0
uniq = [simple_lst[0]]
while(i < len(simple_lst)):
    res = is_uniq(uniq, simple_lst[i])
    if(res == True):
        uniq.append(simple_lst[i])
    i += 1
print("uniq = ", uniq)
