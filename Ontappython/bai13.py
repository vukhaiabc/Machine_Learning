"""
Giả sử đầu vào là: hello world and practice makes perfect and hello world again.
Thì đầu ra là: again and hello makes perfect practice world
"""
s = input("nhap chuoi : ")
lst = s.split(" ")
res = sorted(list(set(lst)))
print(*res)