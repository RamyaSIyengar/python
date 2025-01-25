

# Python program using the List
# slicing approach to rotate the array
def rotateList(arr, d):
  arr = arr[d:] + arr[:d]
  return arr
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6]
print(arr)
print("Rotated list is")
print(rotateList(arr,2))


# -------------------------------
list = [1, 2, 3, 4]

a, *b, c = list
list = [c, *b, a]
print(list)

