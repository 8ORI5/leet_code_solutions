"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity: O(n)
        # Space complexity: O(n)
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return [hash_map[nums[i]], i]
            hash_map[target - nums[i]] = i


                    