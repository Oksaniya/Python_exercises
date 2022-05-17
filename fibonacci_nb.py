def fibonacci(n):
    i = 2
    l = [0,1]
    if(n < 0):
        print("Incorrect input")
    while(i <= n):
        l.append(l[i - 1] + l[i - 2])
        i += 1
    return l[n]
#driver code:
n = 9
print(fibonacci(n))