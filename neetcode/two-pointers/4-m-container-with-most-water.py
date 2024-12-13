"""
Container With Most Water
You are given an integer array heights where heights[i] represents the height
of the i'th bar.

You may choose any two bars to form a container. Return the maximum amount of
water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:
2 <= height.length <= 1000
0 <= height[i] <= 1000
"""
from typing import List


# class Solution():
#     def maxArea(self, heights: List[int]) -> int:
#         res = 0
#
#         for i in range(len(heights)):
#             for j in range(i + 1, len(heights)):
#                 res = max(res, min(heights[i], heights[j]) * (j - i))
#
#         return res

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            # if the left height is smaller than the right, move the left
            if heights[l] <= heights[r]:
                l += 1
            # else move the right
            else:
                r -= 1

        return res


height = [1, 7, 2, 5, 12, 3, 500, 500, 7, 8, 4, 7, 3, 6]
# height = [1, 7, 2, 5, 4, 7, 3, 6]
print(Solution().maxArea(height))
