

def bubblesort(a):

    for i in range(len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


list1 = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubblesort(list1)
print(f"sorted arr", sorted_arr)



"""
- **Basic Concept:** Repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order
- **Implementation Details:**
    - Outer loop (i) runs n times through the array
    - Inner loop (j) compares adjacent elements
    - Swapping occurs when arr[j] > arr[j+1]
- **Step-by-Step Example for [64, 34, 25]:**
    - First Pass: [34, 64, 25] → [34, 25, 64]
    - Second Pass: [25, 34, 64]
    - Third Pass: No swaps needed, array is sorted
- **Efficiency:**
    - Time Complexity: O(n²) in worst and average cases
    - Space Complexity: O(1) as it sorts in-place
"""