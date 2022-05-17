lst = [5, 6, [], 3, [], [], 9]
print("Original list:", lst)

for i in range(len(lst)):
    if(lst[i] != []):
        print(lst[i], end = ', ')