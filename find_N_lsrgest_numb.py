def find_large(lst, n):
    lst.sort()
    lst1 = []
    print("sorted lst: ", lst)
    i = 0
    while(i < len(lst)):
        if(i >= (len(lst) - n)):
            lst1.append(lst[i])
        i += 1
    return lst1


# Driver code
lst = [2, 6, 41, 85, 0, 3, 7, 6, 10]
n = 2
lst1 = find_large(lst, n)
print(lst1)