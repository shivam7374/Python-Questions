x=[str(x) for x in input("\n Enter n alphabets of 1st list ").split() ]
y=[str(x) for x in input("\n Enter n alphabets of 2nd list").split() ]
for (a,b) in zip(x,y):
    print(a,b)