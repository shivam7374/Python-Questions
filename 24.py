x=[str(x) for x in input("\n Enter n alphabets\n").split() ]
n=int(input("enter n\n"))
z=[]
for j in range(0,n):
    y=[]
    for i in range(j,len(x),n):
        y.append(x[i])
    z.append(y)
print(z)