# trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả các chữ số trong số đó là số chẵn
def ktra(i):
    n = str(i)
    if(int(n[0])%2 == 0) and (int(n[1])%2 == 0) and (int(n[2])%2 == 0) and (int(n[3])%2 == 0) :
        return True
    return False
lst =[]
for i in range(1000,3001) :
    if ktra(i) == True:
        lst.append(i)
print(*lst)