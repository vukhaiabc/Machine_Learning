# cac phep toan trên ma trận vs numpy
import numpy as np
a = np.arange(1,13,dtype = float).reshape(3,4)
b = np.arange(2,14,dtype = float).reshape(3,4)
#print(b)
rs_add = a + b
print("Phep cong : \n",rs_add)
rs_sub = b - a
print("Phep tru : \n",rs_sub)
rs_mul = a * b
print(a)
print(b)
print("Phep nhan từng phần tử với nhau  : \n",rs_mul) #khong phản nhân ma trận
rs_div = np.divide(b,a)
print("Phep chia từng phần tử với nhau  : \n",rs_div)
b = b.reshape(4,3) # doi chieu cho b
print(b)
rs_dot = np.dot(a,b)
print("Phep nhan ma trận : \n",rs_dot)

rs_exp = np.exp(a)
print("e mũ từng phần tử của ma trận : ",rs_exp)
rs_log = np.log(rs_exp)
print("lay Ln của từng phần tử : ",rs_log)
bool_arr = np.in1d(a,[3,6,8])
print("Kiem tra [3,6,8] có trong ma trận :  \n",bool_arr)
# con sin cos,sqrt ....