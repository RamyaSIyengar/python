# Given an array of integers nums and an integer
# target,return indices of the two numbers such that
# they add up to target.

# Example
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].

class Solution:

    def twoSum(self, arr, target):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == target:
                    return [i, j]
        else:
            return []


a = [1, 3, 4, 7]
s = Solution()
print(s.twoSum(a, 5))
