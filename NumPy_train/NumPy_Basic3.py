#thuc hien so sanh, tim min max, tính tổng ma trận
import numpy as np
a = np.arange(1,13,dtype = float).reshape(3,4)
b = np.arange(2,14,dtype = float).reshape(3,4)
a[1,0] = 15
print(a)
print("hàng 1 : ",a[1]) # lấy hàng 1
print(a[:,1]) #lay cot 1
c = a[::-1] #dao lai nhung theo hang
print("Đảo ngược các hàng : ",c)
print("Lát cắt ma trận : ")
print("lấy các phần tử của cột 1, hàng 0,1,2  : ",a[0:3,1])
#print(a[:,1:3])

tong = np.sum(a)
print("Tổng các phần tử của ma trận : ",tong)
rs_min = np.min(a)
print(rs_min)
rs_max = np.max(a)
print("Giá trị lớn nhất của MT : ",rs_max)
arr_max = np.max(a,axis=1) #axis = 1 ==> Cột có giá trị max : lấy giá trị max của các hàng ghép thành 1 cột
print("Hàng có giá trị lớn nhất : ",arr_max)
rs_mean = np.mean(a)
print("Giá trị tb của arr : ",round(rs_mean,2))
rs_std = np.std(a)
print("Giá trị đạo hàm của mảng a : ",rs_std)

arr_transpose = np.transpose(a)
print("Ma trận chuyển vị của a : \n",arr_transpose)
arr_Flatten = np.ravel(a)
print("CHuyển về ma trạn 1 chiều :",arr_Flatten)

print("Append 2 ma trận : ",np.append(a,b)) #sẽ làm phẳng ma trận ra
arr_vstack = np.vstack((a,b)) #ngoài ra còn dùng np.concatenate((a,b),axis = 0),np.r_[a,b]
print("Hợp 2 ma trận với nhau (chồng thêm hàng) : \n",arr_vstack)
print("Hợp 2 ma trận với nhau (chồng thêm cột) : \n",np.hstack((a,b)))