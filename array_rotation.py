# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.


#def rot_arr(arr, l, n):
 #   arr2 = [0, 0, 0, 0, 0, 0, 0, 0]
 #   i = 0
  #  while(i < l):
   #     arr2.append(arr[n])
    #    i += 1
     #   n += 1
    #return (arr2)

#def rot_arr(arr, l, n):
 #   i = 0
 #   arr2 = []
 #   while(i < n):
 #       arr2[i] = arr[n]
 #       arr.pop(i)
 #       i += 1
 #       n += 1
 #   i = 0
   # while(i < n):
  #      arr.append(arr2[i])
 #       i += 1

def rot_arr(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i += 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i += 1
        d += 1
    arr[:] = arr[: i] + temp
    return arr
arr = [12, 10, 5, 6, 52, 36]

print("Array after left rotation is: ", end=' ')
print(rot_arr(arr, len(arr), 2))