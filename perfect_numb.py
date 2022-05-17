n = 28
l = []
i = 1
while(i < n):
    if(n % i == 0):
        l.append(i)
    i += 1
print(l)
res = sum(l)
if(res == n):
    print("Yes", n, "is a perfect number")
else:
    print("No", n, "is not a perfect number")