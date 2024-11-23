"""
Two Integer Sum
Given an array of integers nums and an integer target, return the indices
i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that
satisfy the condition.

Return the answer with the smaller index first.

Example 1:
Input:
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000

Notes:
    Input: 
        - Array of Integers
        - Integer target
    Output:
        - Array with two indices that sum up the target 
    
    - Every Array of integers has exactly one pair of output
    - Return the answer with the smaller index first
    - Iterate through array
    - Check if number to get target is already in hashmap
    - Use hashmap to store {value: index}
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            addend = target - nums[i]
            if addend in hash:
                return [hash[addend], i]
            hash[nums[i]] = i
        return [0, 1]


print(Solution().twoSum([3, 2, 3], 6))
