def giaithua(n):
    if n == 0 : return 1
    else : return n*giaithua(n-1)
n = int(input("nhap vao so nguyen : "))
print(giaithua(n))