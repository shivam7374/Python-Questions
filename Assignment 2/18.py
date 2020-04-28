#18
original_lst = [[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
print("Given list : ",original_lst)
highest = original_lst[0]
for item in original_lst:
    if sum(highest) < sum(item):
        highest = item
print("Ans : ",highest)