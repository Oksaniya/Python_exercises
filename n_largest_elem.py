# Given a list of integers, the task is to find N largest elements
# assuming size of list is greater than or equal o N.
lst = [2, 6, 41, 85, 0, 3, 7, 6, 10]
n = 2
for i in range(n):
    print(max(lst))
    lst.remove(max(lst))