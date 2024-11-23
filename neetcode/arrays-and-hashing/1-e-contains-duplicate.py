"""
Duplicate Integer
Given an integer array nums, return true if any value appears more than once
in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]
Output: false

Notes:
    Input: 
        - Array of nums
    Output boolean:
        - True if any value appears more than once
        - False if no value appears more than once
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False


print("contains dupes:", Solution().hasDuplicate([1, 2, 3, 3]))
print("no dupes:", Solution().hasDuplicate([1, 2, 3, 4]))
