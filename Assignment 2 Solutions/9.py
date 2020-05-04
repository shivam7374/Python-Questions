def merge(L1,L2):
    L=[]
    a=len(L1)
    b=len(L2)
    c=min(a,b)
    for i in range(c):
        L.append(min(L1[i],L2[i]))
        L.append(max(L1[i],L2[i]))
    if a>b:
        L.extend(L1[c:])
    if a<b:
        L.extend(L2[c:])
    else:
        return L
    return L