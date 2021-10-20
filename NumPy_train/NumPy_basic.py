import numpy as np
from pprint import pprint as pp
a = np.array([(2,3,4),(3,4,5)])
a1 = np.array([[(1,2,3),(4,5,6)],[(1,2,3),(4,5,6)]])
print(a)
print("Ma tran 2chieu ",a.shape)
print(a1)
print("Ma tran 3 chieu ",a1.shape)

# random ma tran :
print(" ___RanDom Ma Tran___")
a2 = np.random.normal(size=(3,3))
print(a2)

print("___Ma tran full gia tri 0 :")
a3 = np.zeros((3,3),dtype=int)
print(a3)
print("___Ma tran full gia tri 1 :")
a4 = np.zeros((3,4),dtype=float)
print(a4)

print("___Tao ma tran tu 0 --> n-1 :") #co buoc nhảy mỗi phần tử trong mảng
a5 = np.arange(10) #co the cho chay gia tri a5 = np.arange(5,25,4), buoc nhay 4
a5 = np.arange(5,25,4) #không lấy GT = 25
print(a5)
print("___Ma tran chia đều từ cận dưới --> cận trên : ")
a6 = np.linspace(0,10,5) #lấy cả gt = 10
print(a6)
print("___Tao Ma tran full 1 gia tri cho trước : ")
a7 = np.full((2,2),8)  # ma tran 2*2 gia tri full 8
print(a7)
print("___Tao Ma tran don vi duong cheo (1,0) : ")
a8 = np.eye(4) #4 hàng 4 cột
print(a8)
print("___Random Ma Tran : ")
a9 = np.random.random((2,2))
print(a9)