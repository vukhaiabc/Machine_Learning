import re
s = "   quAng     khaI   ptIt  "
s = s.strip()
s = re.sub('\s+'," ",s)
lst = s.split(" ")
res=''
for item in lst:
    res+=item.capitalize()
    if item != lst[-1] :
        res+=' '
print(res)