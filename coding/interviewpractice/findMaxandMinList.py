lst = [63, 54, 32, 90, 1]

maxNo = lst[0]
minNo = lst[0]


for i in range(len(lst)):
    maxNo = max(maxNo, lst[i])
    minNo = min(minNo, lst[i])


print(maxNo)
print(minNo)