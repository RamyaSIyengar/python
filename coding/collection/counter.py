from collections import Counter

l = [1,1,1,1,32,33,33,33,33]
print(Counter(l))  # Counter({1: 4, 33: 4, 32: 1})
c = Counter(l)
print(list(c.elements()))   # [1, 1, 1, 1, 32, 33, 33, 33, 33]
print(c.most_common())   # [(1, 4), (33, 4), (32, 1)]

s = {1: 2, 33: 1}
c.subtract(s)
print(c)  # Counter({33: 3, 1: 2, 32: 1})

