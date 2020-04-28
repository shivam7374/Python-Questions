while(1):
    s=input()
    L=s.split()
    def check(string, sub_str): 
        if (string.find(sub_str) == -1): 
            return False 
        else: 
            return True
    if check(s,"not"):
        for i in range(len(L)):
            if L[i]=="not":
                a=i
                for j in range(i+1,len(L)):
                    if L[j]=="poor":
                        b=j
        print(' '.join(L[0:a])+" good"+' '.join(L[j+1:len(L)])+s[-1])
    else:
        print(s)