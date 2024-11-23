"""
Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents a valid arithmetic
    expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Example 1:
Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5

Constraints:
1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the
    range [-100, 100].
"""

from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))

        return stack[0]

        # [0] [2] [1] [4] [3] [6] [5]
        # ((1 + 2) * 3) - 4 = 5
        # isNumeric
        # hastable of operands
        # stack

        # for c in tokens:
        # if t.strip("-").isnumeric():
        #     stack.append(t)
        # else:
        #     operandOne = stack.pop()
        #     operandTwo = stack.pop()
        #     stack.append(
        #         math.trunc(eval(f'{operandTwo}{t}{operandOne}')))


# print(Solution().evalRPN(["1", "2", "+", "3", "*", "4", "-"]))  # 5
print(Solution().evalRPN(["10", "6", "9", "3", "+",
      "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
