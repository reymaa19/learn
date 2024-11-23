"""
Products of Array Discluding Self
Given an integer array nums, return an array output where output[i] is the
product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20

Notes:
    Input:
        - Array of Integers
    Output:
        - Array where each index is the sum of all numbers except itself

    - First pass = Calculate prefix products from left to right
    - Second pass = Calculate postfix products from right to left and combine

    - Imagine you have 4 cards with numbers
    - For each card, we want to multiply ALL the OTHER numbers EXCEPT itself.

    - Like This:
    - For 1st card: 2 x 4 x 6 = 48
    - For 2nd card: 1 x 4 x 6 = 24
    - For 3rd card: 1 x 2 x 6 = 12
    - For 4th card: 1 x 2 x 4 = 8
    - How the Code Does It
    - It's like having two helpers that walk from both ends of the cards:

    - Helper 1 starts from left, multiplying numbers
    - Helper 2 starts from right, multiplying numbers
    - They work together in one go to fill in all the answers!
    - Final Answer
    - Think of it like skipping one number at a time and multiplying all the
        others - that's all it does! 🎴✨
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s, same length as nums
        res = [1] * (len(nums))

        prefix = 1  # Initialize prefix product to 1
        for i in range(len(nums)):  # Calculate prefix products for each element
            res[i] = prefix  # Set the current result to the prefix product
            prefix *= nums[i]  # Update the prefix product

        postfix = 1  # Initialize postfix product to 1
        for i in range(len(nums) - 1, -1, -1):  # Calculate postfix products for each element
            res[i] *= postfix  # Multiply the current result by the postfix product
            postfix *= nums[i]  # Update the postfix product

        return res  # Return the result array


print(Solution().productExceptSelf([1, 2, 4, 6]))  # [48, 24, 12, 8]

"""
num: [1, 2, 4, 6]

[num[i]*num[i-1], ...]
[1*1, 1*1, 1*2, 4*2] no prefix at index 0 so multiply by 1
pre: [1, 1, 2, 8] Compute the prefix by iterating from the start of the array

[num[-i]*num[-i+1], ...]
[1*48, 2*24, 4*6, 6*1] no postfix at index 3 so multiply by 1
pos: [48, 48, 24, 6] Compute the postfix by iterating from the end of the array

[pre[i]*pos[i+1], ...]
[1*48, 1*24, 2*6, 8*1] no postfix at index 3 so multiply by 1
res: [48, 24, 12, 8] multiply pre[i] and pos[i+1] to get the result

Prefix products at each step:
i=0: [1, 1, 1, 1] * pre=1  -> [1, 1, 1, 1]
i=1: [1, 1, 1, 1] * pre=1  -> [1, 1, 1, 1]
i=2: [1, 1, 1, 1] * pre=2  -> [1, 1, 2, 1]
i=3: [1, 1, 2, 1] * pre=8  -> [1, 1, 2, 8]

Postfix products at each step:
i=0: [1, 1, 2, 8] * post=1 -> [1, 1, 2, 8]
i=1: [1, 1, 2, 8] * post=6 -> [1, 1, 12, 8]
i=2: [1, 24, 12, 8] * post=24 -> [1, 24, 12, 8]
i=3: [48, 24, 12, 8] * post=48 -> [48, 24, 12, 8]

Final result: [48, 24, 12, 8]
Each number is product of all elements except self
"""
