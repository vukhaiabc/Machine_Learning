# a+aa+aaa+aaaa
a = int(input("nhap vao so nguyen : ")) #1
kq = 0
n = 0
t=4
while t :
    n =  n*10 + a
    kq+=n
    t-=1
print(kq)