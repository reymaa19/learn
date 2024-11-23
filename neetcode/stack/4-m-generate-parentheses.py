"""
Generate Parentheses
You are given an integer n. Return all well-formed parentheses strings that you
can generate with n pairs of parentheses.

Example 1:
Input: n = 1
Output: ["()"]

Example 2:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

You may return the answer in any order.

Constraints:
1 <= n <= 7

Notes:
    - Input:
        - n of how many parentheses
    - Output
        - Array of string of paretheses combinations

    ((())) o,o,o,c,c,c
    (()()) o,o,c,o,c,c
    (())() o,o,c,c,o,c
    ()(()) o,c,o,o,c,c
    ()()() o,c,o,c,o,c
    output is an array of strings
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parantheses if closed < n
        # only adda a closing parantheses if closed < open
        # valid if open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()  # this goes back (look into this)

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


print(["((()))", "(()())", "(())()", "()(())", "()()()"])
print(Solution().generateParenthesis(3))
