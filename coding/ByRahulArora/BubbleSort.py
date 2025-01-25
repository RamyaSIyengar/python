'''
Variable 'minVal' = array[0]
For each element in the array
    If current element < minVal
        minVal = current element
'''
#
my_array = [7, 12, 9, 4, 1]
# minVal = my_array[0]  # Step 1
#
# for i in my_array:  # Step 2
#     if i < minVal:  # Step 3
#         minVal = i
#
# print('Lowest value: ', minVal)  # Step 4


def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap if j > j+1
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break


# when i=0 => range(0, 8-0-1) => range(0, 7), so j goes from 0 to 6.
# when i=1 => range(0, 8-1-1) => range(0, 6), so j goes from 0 to 5.
my_arr = [64, 34, 25, 12, 22, 11, 90, 5]
bubble_sort(my_arr)
print(my_arr)
