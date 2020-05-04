def reverse_v1(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0,word)
  return " ".join(result)
test1 = input("Enter a sentence: ")
print (reverse_v1(test1))