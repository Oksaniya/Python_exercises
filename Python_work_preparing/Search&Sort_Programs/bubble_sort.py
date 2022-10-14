def bubble_sort(lst):
    for i in range(len(lst)):
        for e in range(len(lst) - 1):
            if(lst[e] > lst[e+1]):
                lst[e], lst[e+1] = lst[e+1], lst[e]

# driver code:
lst = [9, 8, 5, 2, 6, 1]
bubble_sort(lst)
print(lst)