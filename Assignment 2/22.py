x=[str(x) for x in input("\n Enter n alphabets").split() ]
a=int(input("\n Enter n \n"))
y=[]
for i in x:
    for j in range(1,(a+1)):
        r=i+str(j)
        y.append(r)
print(y)