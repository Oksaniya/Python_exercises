matrix1 =   [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix2 =   [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

result =    [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

# for i in range(len(matrix1)):
#     for e in range(len(matrix2)):
#         result[i][e] = matrix1[i][e] * matrix2[i][e]
#
# for i in result:
#     print(i)

i = 0
while(i < len(matrix1)):
    e = 0
    while(e < len(matrix2)):
        result[i][e] = matrix1[i][e] * matrix2[i][e]
        e += 1
    i += 1

for i in result:
    print(i)