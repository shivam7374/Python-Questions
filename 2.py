s=input()
a=s[0]
L=[]
for ch in s:
    L.append(ch)
for i in range(1,len(s)):
    if s[i]==a:
        L[i]="$"
print(''.join(L))