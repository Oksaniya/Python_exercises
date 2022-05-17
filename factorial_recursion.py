def factorial(x):
    if (x == 1) or (x == 0):
        return 1
    elif x < 0:
        print("Factorial does not exist for negative numbers")
    else:
        return (x * factorial(x - 1))

num = -8

result = factorial(num)
print("The factorial of", num, "is", result)