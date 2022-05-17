# Given a list of numbers, write a Python program to print all even numbers in the given list.
def even(lst):
    lst1 = []
    for i in range(len(lst)):
        if(lst[i] % 2 == 0):
            lst1.append(lst[i])
    return lst1

def odd(lst):
    lst1 = []
    for i in range(len(lst)):
        if (lst[i] % 2 != 0):
            lst1.append(lst[i])
    return lst1
# driver part
lst = [10, 21, 4, 45, 66, 93]
print("Even numbers of the list:", even(lst))
print("Odd numbers of the list:", odd(lst))

