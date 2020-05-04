#17 
lst = [[10,20],[40],[30,56,25],[10,20],[33],[40]]
a = []
print("Given list : ",lst)
for item in lst:
    if lst.count(item) == 1:
        a.append(item)
    else:
        a.append(item)
        for i in lst:
            if i == item:
                lst.remove(item)
print("Final list : ",a)
