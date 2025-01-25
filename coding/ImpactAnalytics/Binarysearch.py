
def binary_search(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right)//2
        print(left, right, mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(binary_search([1,3,5,6], 2))


"""
Binary Search:

Start with two pointers: left (start of the array) and right (end of the array).
Calculate the middle index as mid = (left + right) // 2.
Compare:

If nums[mid] == target, return mid.
If nums[mid] < target, move the left pointer to mid + 1 (search in the right half).
If nums[mid] > target, move the right pointer to mid - 1 (search in the left half).
Insert Position:

If the target is not found, the left pointer will point to the correct position to insert the target.

Input: nums = [1,3,5,6], target = 5
Steps:
mid = (0 + 3) // 2 = 1, nums[mid] = 3 (less than 5), move left to 2.
mid = (2 + 3) // 2 = 2, nums[mid] = 5 (equal to target), return 2.
Output: 2
"""