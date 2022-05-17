import numpy

A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# 3 x 4
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

C = numpy.dot(A, B)

for i in C:
    print(i)