# 3 x 3
A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# 3 x 4
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

# new matrix 3 x 4
C = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
# i by row of A
for i in range(len(A)):
     # j by column of B
     for j in range(len(B[0])):
          # k by row of B
          for k in range(len(B)):
               C[i][j] += A[i][k] * B[k][j]
for b in C:
     print(b)
