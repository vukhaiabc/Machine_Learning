res = []
while True:
    s = input()
    if s.strip() :
        res.append(s.strip().upper())
    else : break
print(*res)