import re
s = "quang    khai    ptit"
math = re.sub("\s+"," ",s)
if math :
    print(math)
else :
    print("khong tim thay!")