# Python program to find Cumulative sum of a list
def cum_sum(lst):
    l = []
    l.append(lst[0])
    for i in range(1, len(lst)):
        l.append(lst[i] + l[i - 1])
    return l
# driver program
lst = [10, 20, 30, 40, 50]
print(cum_sum(lst))