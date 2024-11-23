"""
Minimum Stack

Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2,
        "push", 0, "getMin", "pop", "top", "getMin"]

Output:
    [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    # My Implementation (Faster and more space efficient)
    # def __init__(self):
    #     self.stack = []
    #     self.min = -2147483648
    #     self.prev_min = -2147483648

    # def push(self, val: int) -> None:
    #     if not self.stack:
    #         self.min = val
    #     else:
    #         self.prev_min = self.min
    #         self.min = min(val, self.min)
    #     self.stack.append(val)

    # def pop(self) -> None:
    #     if self.stack:
    #         popped = self.stack.pop()
    #         if self.min == popped:
    #             if self.stack:
    #                 self.prev_min = self.min
    #                 self.min = min(self.stack)
    #             else:
    #                 self.min = -2147483648
    #                 self.prev_min = -2147483648

    # def top(self) -> int:
    #     if self.stack:
    #         return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.min


minStack = MinStack()
print("None", minStack.push(1))
print("None", minStack.push(2))
print("None", minStack.push(0))
print("0", minStack.getMin())
print("None", minStack.pop())
print("2", minStack.top())
print("1", minStack.getMin())
