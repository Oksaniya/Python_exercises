def odd_numb(lst):
    i = 0
    lst1 = []
    while(i < len(lst)):
        if (lst[i] % 2 != 0):
            lst1.append(lst[i])
        i += 1
    return lst1

def find_square(lst1):
    i = 0
    lst2 = []
    while(i < len(lst1)):
        lst2.append(lst1[i] * lst1[i])
        i += 1
    return lst2

# driver code
lst = [1,2,3,4,5,6,7]
lst1 = odd_numb(lst)
print("odd numbers: ", lst1)
lst2 = find_square(lst1)
print(lst2)