# The original list is :
# [[4, 5, 6],
# [8, 1, 10],
# [7, 12, 5]]
# The 3th column of matrix is : [6, 10, 5]

matrix = [[4, 5, 6],
          [8, 1, 10],
          [7, 12, 5]]

n = 3
n_th_column = []
for i in matrix:
    e = 0
    while(e < len(matrix[0])):
        if(e == (n - 1)):
            n_th_column.append(i[e])
        e += 1
print(n_th_column)
