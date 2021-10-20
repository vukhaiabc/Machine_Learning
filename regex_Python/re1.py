import re
s = 'main'
match = re.match('ma*n',s)
if match:
    print('khop')
else : print("khong khop")