arr = [5, 32, 45, 12, 18, 25]

arr.sort(reverse=True)
print(arr)

diff = arr[0]-arr[len(arr)-1]
print(diff)

for i in range(1, len(arr)-1):
    diff =min(diff, arr[i]-arr[i+1])

print(diff)


#  you can simplify by only checking consecutive elements in the sorted list.
#  Since the list is sorted, the smallest difference will always be between two
#  consecutive elements.