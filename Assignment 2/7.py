def pscltrngl(n):
    
    def fact(n):
        if n==0:
            return 1
        else:
            a=1
            for i in range(1,n+1):
                a=a*i
            return a

    def ncr(n,r):
        return int(fact(n)/(fact(n-r)*fact(r)))
    for i in range(n):
        s=''
        for j in range(i+1):
            s=s+' '+str(ncr(i,j))
        print(s)

n=int(input())
print(pscltrngl(n))