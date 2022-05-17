# Python | Sum of number digits in List
import numpy
def digit_nb(lst):
    lst2 = []
    res = []
    for i in range(len(lst)):
        lst2.append([int(i) for i in str(lst[i])])
    res.append(list(map(sum, list(lst2))))
    return(res)
# driver code
lst = [12, 67, 98, 34]
print(digit_nb(lst))

