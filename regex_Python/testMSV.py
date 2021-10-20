import re
s='b17DcCN337'
pattern = '^B[0|1][0-9]DCCN\d{3}$'
match = re.match(pattern,s,flags=re.IGNORECASE)
if match:
    print("Khop!")
else :
    print("khong khop!")