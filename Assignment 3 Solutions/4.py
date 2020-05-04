def Sort(tup):

    return (sorted(tup, key=lambda x: float(x[1]), reverse=True))


tup = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(Sort(tup))