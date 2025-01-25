# Method which accepts Array and returns sum of all the elements in array

def sum_of_array(arr):
    # extract each element from array and add it to a variable which was initialized with 0
    suma = 0
    for i in range(len(arr)):
        suma = suma + arr[i]
    return suma


# Print Multiplication table without using Multiply operator

def multiple(i, j):
    # i has to add itself by j times; 5*3 => 5 has to add with itself 3 times
    #
    res = 0
    for num in range(j):
        res = res + i
    return res


# Max difference between any adjacent index in array

def maxdiff(arr):
    diff = 0
    for i in range(len(arr)-1):
        diff = a[i+1] - a[i]
    return diff


#  compare same indexes of 2 different arrays and create new array for matchValues
def sameindex_of2arr(arr1, arr2):
    if len(arr1) == len(arr2):
        print(len(arr1), len(arr2))
        arr3 = []
        for i in range(len(arr1)):
            if arr1[i] == arr2[i]:
                arr3.append(arr1[i])
        return arr3


a = [1, 2, 6, 9, 18]
b = [1, 3, 6, 10, 18]
arraySum = sum_of_array(a)
print(arraySum)
mul = multiple(5, 10)
max_difference = maxdiff(a)  # a+1 - a diff = 1, 4, 3, 9
print(mul)
print(max_difference)
newarr = sameindex_of2arr(a, b)
print(newarr)


# for i in range(len(a)):
#     print(a[i])
