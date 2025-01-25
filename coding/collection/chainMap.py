from collections import ChainMap

d1 = {'a' : 1, 'b':2}
d2 = {'b':10, 'y':20}

d12 = ChainMap(d1, d2)  # ChainMap({'a': 1, 'b': 2}, {'b': 10, 'y': 20})
print(list(d12))  # ['b', 'y', 'a']

print(d12['b'])  # 2 from d1
