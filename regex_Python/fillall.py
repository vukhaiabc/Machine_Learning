import re
s="chuoi 3 gom cac so : 24,35,46,37"
match = re.findall("\d+",s)
if match:
    print(match)
else :
    print("k tim thay!")