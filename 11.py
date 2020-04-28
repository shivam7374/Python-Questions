#11
def conversion(s):
    num = 0
    count = len(s)
    for i in s:
        num += (int(i))*(2**(count-1))
        count-=1
    return num
lst = []
a = input("Enter Numbers : ")
b = a.split(",")
for item in b:
    new = conversion(item)
    if new%5 == 0:
        lst.append(item)
print(",".join(lst))