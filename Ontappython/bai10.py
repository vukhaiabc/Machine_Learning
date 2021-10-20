# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
import numpy as np
s = input("nhap vao m,n : ")
lst = [int(x) for x in s.split(",")]
m = lst[0]
n = lst[1]
result = np.zeros((m,n),dtype=int)
for i in range(0,m):
    for j in range(0,n):
        result[i][j] = i*j
print(result)