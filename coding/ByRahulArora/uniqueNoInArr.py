a = [4, 5, 5, 5, 6, 7, 6, 4, 1]
ab = []
for i in a:
    k = 0
    if i not in ab:
        ab = ab.append(i)
print(ab)

