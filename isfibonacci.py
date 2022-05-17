#A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
import math
def is_fibonacci(n):
    var1 = math.sqrt((5 * (n ** 2)) + 4)
    var2 = math.sqrt((5 * (n ** 2)) - 4)
    check_int1 = (var1).is_integer()
    check_int2 = (var2).is_integer()

    if((check_int1 == True) or (check_int2 == True)):
        print("Yes,", n, "is a Fibonacci number")
    else:
        print("No,", n, "is not a Fibonacci number")

#driver part
n = 34
is_fibonacci(n)


