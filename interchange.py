# Python program to interchange first and last elements in a list
def l_swap(l):
    l2 = []
    l2.append(l[len(l) - 1])
    i = 1
    while(i < (len(l) - 1)):
        l2.append(l[i])
        i += 1
    l2.append(l[0])
    return l2

# driver part
l = [12, 35, 9, 56, 24]
print(l_swap(l))