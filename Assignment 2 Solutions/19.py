#19
lst = [1,2,3,4]
new_lst = []
print("Given list :",lst )
a = input("Enter string : ")
for item in lst:
    new_lst.append(a+str(item))
print("New List : ",new_lst)