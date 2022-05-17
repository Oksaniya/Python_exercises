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
start = 2
end = 7
print("Below are all prime numbers from", start, "till", end)
while(start < end):
    if(is_prime(start) == 1):
        print(start, end=" ")
    start += 1