"""
Largest Rectangle In Histogram
You are given an array of integers heights where heights[i] represents the
height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:
Input: heights = [7,1,7,2,2,4]
Output: 8

Example 2:
Input: heights = [1,3,7]
Output: 7

Constraints:
1 <= heights.length <= 1000.
0 <= heights[i] <= 1000

Notes:
    Input:
        - array of integers
            - heights where heights[i] is the height of bar
            - each bar has a width of 1
    output:
        - the largest rectagnle that can be formed among the bars
"""
from typing import List

# TODO:
# - only use 1 stack


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        combinations = {}
        allCombs = []

        for i, height in enumerate(heights):
            current = (height, 1)
            combinations.setdefault(i, []).append(current)

            if not i == 0:
                for j, comb in enumerate(combinations[i-1]):
                    lowestCommonHeight = min(comb[0], height)
                    combinations[i].append((lowestCommonHeight, comb[1] + 1))

        for i, c in combinations.items():
            for j, comb in enumerate(c):
                allCombs.append(comb[0] * comb[1])

        return max(allCombs)


print("solution:", Solution().largestRectangleArea([7, 1, 7, 2, 2, 4]))
