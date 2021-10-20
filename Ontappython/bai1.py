lst = []
for num in range(2000,3201):
    if (num%7 == 0) and (num % 5 !=0) :
        lst.append(str(num))
print(*lst)