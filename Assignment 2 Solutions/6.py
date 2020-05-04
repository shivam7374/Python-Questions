s=input()
L=[]
for ch in s:
    if not ch in L:
        L.append(ch)
for ch2 in L:
    a=s.count(ch2)
    if a>1:
        print(ch2+''+str(a))