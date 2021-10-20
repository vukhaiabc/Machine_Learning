import re
s = "vu van khai quangkhaiptit"
match = re.match("vu van khai",s)
if match :
    print(match.group())
else :
    print("khong thay!")