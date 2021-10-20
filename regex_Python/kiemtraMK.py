"""
1. Ít nhất 1 chữ cái nằm trong [a-z]
2. Ít nhất 1 số nằm trong [0-9]
3. Ít nhất 1 kí tự nằm trong [A-Z]
4. Ít nhất 1 ký tự nằm trong [$ # @]
5. Độ dài mật khẩu tối thiểu: 6
6. Độ dài mật khẩu tối đa: 12
"""
import re
listpass = [x.strip() for x in input("nhap cac Mk:").split(',')]
res =[]
def kt(s):
    flag = False
    if len(s) >= 6 and len(s) <= 12 :
        if (re.search('[a-z]',s)) and (re.search('[A-Z]',s))and(re.search('[0-9]',s)) and (re.search('[$ # @]',s)):
            flag = True
    return flag
for item in listpass:
    if kt(item):
        res.append(item)
print(*res)