arr = [5, 7, 4, 3, 9, 8, 19, 21, 10]
sum1 = 17

# print(sorted(arr))
lis = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        # print(i,j)
        if arr[i]+arr[j] == sum1:
            print(arr[i],arr[j], sum1)
            lis.append((arr[i],arr[j]))

print(lis)

# Looping through the list:
# The outer loop for i in range(len(arr)) selects each element arr[i].
# The inner loop for j in range(i+1, len(arr)) selects each element arr[j]
# starting from i+1 to avoid comparing the same pair more than once.

