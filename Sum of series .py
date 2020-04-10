n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n):
    sum1=sum1+(i/i+1)
print("The sum of series is",round(sum1,2))
