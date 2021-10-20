# without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
s = input("nhap vao chuoi : ")
lst = s.split(",")
res = sorted(lst,reverse=True)
print(lst)
print(res)