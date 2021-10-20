import re
s = "vu van khai quangkhaiptit"
match = re.search('quangkhaiptit',s)
if match :
    print(match.group())
else : print("khong thay!")