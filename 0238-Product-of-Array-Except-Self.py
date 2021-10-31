"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        # based on the index of the number, pop the number and multiply the product of the rest of the numbers
        # then append the product to the result list
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        return result


           