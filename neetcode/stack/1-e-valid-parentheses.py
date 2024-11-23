"""
Valid Parentheses

You are given a string s consisting of the following characters:
    '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    Return true if s is a valid string, and false otherwise.

Example 1:
    Input: s = "[]"
    Output: true

Example 2:
    Input: s = "([{}])"
    Output: true

Example 3:
    Input: s = "[(])"
    Output: false

Explanation:
    The brackets are not closed in the correct order.

Constraints:
    1 <= s.length <= 1000

Notes:
    Input:
        - String of parentheses
    Output:
        - Boolean value of whether the parentheses are valid

Stack:
    - Last In Last Out (LIFO)
    - append(el): Adds an en element to the top of the Stack
    - pop(): Removes and returns the top element from the Stack

Rules:
    - if the start is a closed bracket return false
    - if the start is a type of open bracket continue
    - continue onto the next iteration until the bracket is a closed bracket
    - if the closed bracket is not the in the correct order return false
    - if the closed bracket is in the correct order pop from the stack
    - return true if the stack is empty, false if not
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

    # def isValid(self, s: str) -> bool:
    #     open = {"(": "round", "[": "square", "{": "curly"}
    #     closed = {")": "round", "]": "square", "}": "curly"}
    #     stack = []
    #
    #     for p in s:
    #         if p in open:
    #             stack.append(p)
    #         elif len(stack) == 0:
    #             return False
    #         elif p in closed and closed.get(p) == open.get(stack[-1]):
    #             stack.pop()
    #         else:
    #             return False
    #
    #     if len(stack) > 0:
    #         return False
    #     return True


print(Solution.isValid(Solution, "([{}])"))  # True
