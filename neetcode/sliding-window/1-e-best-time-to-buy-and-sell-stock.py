"""
Best Time to Buy and Sell Stock
You are given an integer array prices where prices[i] is the price of NeetCoin
on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in
the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any
transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:
1 <= prices.length <= 100
0 <= prices[i] <= 100
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return 1


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))

#     l, r = 0, 1  # left = buy, right = sell
#     maxP = 0
#
#     # buy low sell high
#     while r < len(prices):  # keep iterating until the end
#         if prices[l] < prices[r]:  # if profitable
#             profit = prices[r] - prices[l]
#             maxP = max(maxP, profit)
#         else:
#             l = r  # shift l to r since its the new cheapest price
#         r += 1  # update the r pointer since time moves in one direction
#
#     return maxP
#
# # O(n^2)
# # def maxProfit(self, prices: List[int]) -> int:
# #     res = 0
# #
# #     for i in range(len(prices)):
# #         for j in range(i + 1, len(prices)):
# #             profit = prices[j] - prices[i]
# #             res = max(profit, res)
# #
# #     return res
