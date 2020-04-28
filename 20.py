#20
lst1 = ["red","orange","green","blue","white"]
lst2 = ["black","yellow","green","blue"]
print("Given list : ")
print(lst1)
print(lst2)
s1 = set(lst1)
s2 = set(lst2)
ans1 = list(s1-s2)
ans2 = list(s2-s1)
print("Output : ")
print(ans1)
print(ans2)