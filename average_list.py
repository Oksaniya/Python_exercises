def average(lst):
    n = len(lst)
    s = lst[0]
    for i in range(n - 1):
        s = s + lst[i + 1]
    res = s / n
    return res
# driver code
lst = [15, 9, 55, 41, 35, 20, 62, 49]
print("The average of the list is")
print(average(lst))