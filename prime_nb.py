def is_prime(n):
    i = 1
    e = 0
    for t in range(n):
        if(n % i == 0):
            e += 1
        i += 1
    if(e == 2):
        return 1
    else:
        return 2

# Driver program
n = 11
print("Below are all prime numbers till", n)
for i in range(n + 1):
    if(is_prime(i) == 1):
        print(i, end=" ")
    i += 1