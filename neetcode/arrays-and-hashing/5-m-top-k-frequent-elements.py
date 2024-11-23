"""
Top K Elements in List
Given an integer array nums and an integer k, return the k most frequent 
elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

Notes: 
    Input: 
        - Array of Integers nums
        - Integer target k, where k is the minimum frequency of numbers
            appearing in the Array of nums
    Output:
        - The Integers that appear minimum k amount

    - Use bucket sort
    - Max length of freq dict of length nums
    - Use count occurance of nums as the key
    - Iterate through the freq backwards and append to the result until k length
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, count in count.items():
            freq[count].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res


print(Solution().topKFrequent([1, 2, 2, 3, 3, 3], 2))
