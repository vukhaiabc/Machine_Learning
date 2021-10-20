# dem chu so, chu cai
s = input("nhap chuoi : ")
kq = 0
kq1 = 0
for i in range(0,len(s)):
    if s[i].isalpha():
        kq+=1
    if s[i].isdigit():
        kq1+=1
print("chu cai : ",kq)
print("chu so : ",kq1)