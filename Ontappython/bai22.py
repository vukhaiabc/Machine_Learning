lst =[]
def sort(item):
    return item[0],item[1],item[2]
while True:
    s = input()
    if not s :
        break
    else :
        lst.append(tuple(s.split(",")))
lst.sort(key=sort)
print(lst)