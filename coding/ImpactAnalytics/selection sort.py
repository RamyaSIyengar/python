l = [11,2,4,1,55,3, 22]

for i in range(len(l)):
    min_indx = i
    for j in range(i+1, len(l)):
        if l[j] < l[min_indx]:
            l[j], l[min_indx] = l[min_indx], l[j]
print(l)

"""
- Bubble Sort works by repeatedly swapping adjacent elements if they are in wrong order
- Selection Sort works by repeatedly finding the minimum element from unsorted portion

**Let's walk through Selection Sort iterations for array [64, 34, 25, 12, 22, 11, 90]:**

- Iteration 1: Find minimum in entire array
    - Minimum found: 11 (at index 5)
    - Swap with first element: [11, 34, 25, 12, 22, 64, 90]
- Iteration 2: Find minimum in array[1:end]
    - Minimum found: 12 (at index 3)
    - Swap with second element: [11, 12, 25, 34, 22, 64, 90]
- Iteration 3: Find minimum in array[2:end]
    - Minimum found: 22 (at index 4)
    - Swap with third element: [11, 12, 22, 34, 25, 64, 90]
- Iteration 4: Find minimum in array[3:end]
    - Minimum found: 25 (at index 4)
    - Swap with fourth element: [11, 12, 22, 25, 34, 64, 90]

"""