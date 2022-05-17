#Reconstruct the array by replacing arr[i] with (arr[i-1]+1) % M
def construct(n, m, arr):
    i = 1
    while(i < n):
        arr[i] = (arr[i-1]+1) % m
        i += 1
    return arr
# Driver code
n, m = 6, 7
arr = [5, -1, -1, 1, 2, 3]
print(construct(n, m, arr))