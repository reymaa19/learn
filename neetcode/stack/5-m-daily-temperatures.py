"""
Daily Temperatures
You are given an array of integers temperatures where temperatures[i]
represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day
before a warmer temperature appears on a future day. If there is no day in the
future where a warmer temperature will appear for the ith day, set result[i] to
0 instead.

Example 1:
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Example 2:
Input: temperatures = [22,21,20]
Output: [0,0,0]

Constraints:
1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100

Notes:
    Input:
    - array of integers where temperatures[i] is the temperature for that day
    Output:
    - return an array with result[i] as the number of days after it gets warmer
    - If there are no days after it gets warmer, result[i] is 0
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic stack
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])

        return res


# [8,1,5,4,3,2,1,1,0,0]
print(Solution().dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
