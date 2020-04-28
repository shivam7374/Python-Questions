def func(s):
    c1=0
    c2=0
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                c1+=1
            elif ch.islower():
                c2+=1
    print("No. of Upper case characters : "+str(c1))
    print("No. of Lower case Characters : "+str(c2))