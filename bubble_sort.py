def b_sort(arr):
    n = (len(arr) - 1)
    for i in range(n):
        for j in range(n - i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[j]
# driver code:
arr = [7, 5, 7, 1]
b_sort(arr)
for i in range(len(arr)):
    print ("%d" % arr[i], end=" ")