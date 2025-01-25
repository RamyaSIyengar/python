arr = [[2, 9, 3, 4],
       [1, 49, 5, 3],
       [7, 9, 2, 11]]

mini = maxi = arr[0][0]
for i in arr:
    for j in i:
        if j < mini:
            mini = j
        if j > maxi:
            maxi = j
        print(j, end=' ')
    print()
print(mini)
print(maxi)
