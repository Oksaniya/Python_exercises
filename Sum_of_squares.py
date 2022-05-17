#Python Program for Sum of squares of first n natural numbers
n = 5
i = 1
list = []
while(i <= n):
    list.append(i ** 2)
    i += 1
print(sum(list))
