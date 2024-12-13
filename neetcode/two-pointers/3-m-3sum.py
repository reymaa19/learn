"""
3Sum
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0,
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets.
You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""
from typing import List

# triplet if numbers i + j + k == 0 and i, j, k are not duplicates
# goal is 3 numbers to equal 0
# keep track of numbers that make it impossible to equal to 0?
# two pointers from base to operand

# USE TWO POINTERS twosum II


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            # Start a at index 1
            if n > 0:
                break

            # Check for duplicates
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = n + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])

                    l += 1

                    # Update left pointer until a non duplicate value is found
                    # and don't go past the right pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))  # [[-1,-1,2],[-1,0,1]]
