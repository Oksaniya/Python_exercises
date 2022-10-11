def search_place(tab1, tab2):
    i = 0
    res = 0
    while(i < len(tab2)):
        if(tab1[i] != tab2[i]):
            res = i
            break
        i += 1
    if(res == 0):
        res = len(tab1)
    return res

# driver code
# 2 tab 1 - 4 elem, 2 - 5 elem. 4 elem - jednakowe w roz kol
tab1 = [1,2,3,4,5]
tab2 = [1,3,5,4]
list.sort(tab1)
list.sort(tab2)
print(tab1)
print(tab2)
ith = search_place(tab1, tab2)
print(ith)
print("newystracz. elem is:", tab1[ith])
