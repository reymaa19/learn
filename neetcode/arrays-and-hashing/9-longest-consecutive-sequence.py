"""
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive
    sequence of elements.

A consecutive sequence is a sequence of elements in which each element is
    exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4

Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

Notes:
    - Input:
        - Array of Integers nums
    - Output:
        - Integer of the longest consecutive sequence of numbers

    - Keep track of number appearance
    - Keep track of longest streak
    - If current number + 1 found in hashmap
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_len = 0
        tbl = dict()
        for num in nums:
            # get the length for num - 1 sequence formed so far
            left = tbl.get(num-1, 0)
            # get the length for num + 1 sequence formed so far
            right = tbl.get(num+1, 0)
            # calculate the current sequnce length possible
            curr_len = right + left + 1
            # set the sequence length for starting index
            # to find starting index just subtract current num - l
            # each step was 1 and we just moved l*1 from num to get the start
            tbl[num - left] = curr_len
            # similar for the rightmost
            tbl[num + right] = curr_len
            longest_len = max(curr_len, longest_len)
        return longest_len

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     numSet = set(nums)
    #     longest = 0
    #
    #     for n in nums:
    #         if (n - 1) not in numSet:  # check if its a start of a sequence
    #             sequence = 0  # initialize the start of a sequence
    #
    #             while (n + sequence) in numSet:  # if next number exists
    #                 sequence += 1  # increase the length of the sequence
    #
    #             if sequence > longest:
    #                 longest = sequence
    #
    #     return longest


print(Solution().longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
print(Solution().longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))
