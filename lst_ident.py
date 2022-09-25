def check(lst):
    copy_lst = lst
    for i in range(len(lst)):
        k = 0
        for j in range(len(copy_lst)):
            if ((lst[i] == copy_lst[j]) and (k == 0)):
                k += 1
            elif((lst[i] == copy_lst[j]) and (k == 1)):
                return True
    return False

# driver code
lst = [5, 7, 9, 6, 2, 11]
print(check(lst))