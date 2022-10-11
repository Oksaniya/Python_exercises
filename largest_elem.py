#Python Program to find largest element in an array
arr = [10, 45, 99, 98]
arr.sort()
print(arr[-1], arr[-2])
#i = 1
#n = arr[0]
#while(i < len(arr)):
#    if((arr[i - 1] < arr[i]) and (arr[i] > n)):
#        n = arr[i]
#    elif((arr[i - 1] < arr[i]) and (arr[i] < n)):
#        n = n
#    else:
#        n = arr[i - 1]
#    i += 1
#print(n)