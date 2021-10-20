'''
Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H])
(bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
 Với giá trị cố định của C là 50, H là 30.
 D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.
'''
import math
s = input("nhap vao gia tri : ")
lst = s.split(",");
c = 50
h = 30
res = []
for D in lst:
    Q = int(math.sqrt((2 * c * int(D))/h))
    res.append(Q)
print(*res)