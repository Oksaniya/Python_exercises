num = input("Enter a number: ")
factorial = 1

if int(num) < 0:
    print("Factorial does not exist for negative numbers")

elif int(num) == 0:
    print("The factorial of 0 is 1")

else:
    for i in range(1, int(num) + 1):
        factorial = factorial * i

    print("The factorial of", format(num), "is", factorial)