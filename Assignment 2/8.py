def func(s):
    L=s.split('-')
    L.sort()
    return '-'.join(L)
s=input()
print(func(s))