def dup(lst):
    lst1 = []
    i = 0
    while(i < len(lst)):
        e = i + 1
        while(e < len(lst)):
            if(lst[i] == lst[e]):
                lst1.append(lst[e])
            e += 1
        i += 1
    lst = list(dict.fromkeys(lst1))
    return lst
# driver part
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(dup(lst))