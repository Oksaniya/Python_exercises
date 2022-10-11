def pos_modify(pos1, pos2):
    lst2 = []
    lst2.append(pos1 - 1)
    lst2.append(pos2 - 1)
    return lst2


def swap_two_elem(lst, lst2):
    i = 0
    lst1 = []
    while(i < len(lst)):
        if((i) == lst2[0]):
            lst1.append(lst[lst2[1]])
        elif((i) == lst2[1]):
            lst1.append(lst[lst2[0]])
        else:
            lst1.append(lst[i])
        i += 1
    return lst1



# driver code
lst = [23, 65, 19, 90]
print(lst)
pos1, pos2 = 1, 3
lst2 = pos_modify(pos1, pos2)
lst1 = swap_two_elem(lst, lst2)
print(lst1)