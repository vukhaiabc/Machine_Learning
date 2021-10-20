n = int(input("nhap vao so nguyen : "))
lst ={}
for i in range(1,n+1):
    lst[i] = i*i;
for item in lst:
    print(item,":",lst.get(item))