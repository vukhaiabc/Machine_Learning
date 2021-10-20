# 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
s = input("nhap chuoi : ")
lst = [x for x in s.split(",") if int(x) %2 ==1]
print(*lst)