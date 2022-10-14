# Input : arr[] = {10, 20, 80, 30, 60, 50,
#                      110, 100, 130, 170}
#           x = 110;
# Output : 6

def pos_search(arr, x):
    i = 0
    res = -1
    while(i < len(arr)):
        if(arr[i] == x):
            res = i
        i += 1
    return res

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110
print("Original arr is: ", arr)
if(pos_search(arr, x) == -1):
    print("there is no this value (", x, ") in array")
else:
    print("The value ", x, "is in position ", pos_search(arr, x))

