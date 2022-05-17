#Input : arr[] = {100, 10, 5, 25, 35, 14},
#            n = 11
#Output : 9
#100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9
import numpy
def math(arr, n):
    m = numpy.prod(arr) % 11
    return m
#driver part
n = 11
arr=[100,10,5,25,35,14]
print(math(arr, n))