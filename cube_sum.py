#Python Program for Sum of cube squares of first n natural numbers
n = 5
i = 1
list = []
while(i <= n):
    list.append(i ** 3)
    i += 1
print(sum(list))
