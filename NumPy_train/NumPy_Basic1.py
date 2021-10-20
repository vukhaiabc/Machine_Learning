# lưu ma trận.npy, .txt và load ma trận

import numpy as np
a = np.load('00mtdonvi.npy')
print(a)
b = np.array([2,3,4])
c = np.arange(5,25,4)
#np.savez('00Luu2matran',b,c)
file = np.load('00luu2matran.npz')
print(file['arr_0']) #in ra mt phan tu thu 1
d = file['arr_1']
print(d)

print("Save and Display ma tran file txt : ")
np.savetxt('00mttxt',d)
matrix_txt = np.loadtxt('00mttxt.txt')
print(matrix_txt)

