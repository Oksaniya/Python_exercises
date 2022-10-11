def remove_last_elem(lst):
    i = 0
    lst1 = []
    while(i < (len(lst) - 1)):
        lst1.append(lst[i])
        i += 1
    print(lst1)

# driver code
lst = ["Geeks", "For", "Geeks1"]
print("Original list: ", lst)
remove_last_elem(lst)

