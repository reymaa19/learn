"""
643. Maximum Average Subarray I
Easy
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error less
than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[0:k])

        # Start the loop from the kth element
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]

            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k


nums = nums = [1, 12, -5, -6, 50, 3]
k = 4

# Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
print(Solution().findMaxAverage(nums, k))  # 12.75000

"""
Explain the following solution for the findMaxAverage function for me

## Copilot ───

Sure, here's an explanation of the `findMaxAverage` function:

The goal of the `findMaxAverage` function is to find the contiguous subarray of
length `k` that has the maximum average value in the given list `nums`.

Here's a step-by-step explanation of the solution:

1. **Initial Sum Calculation**:
   ```python
   current_sum = sum(nums[:k])
   ```
   This line calculates the sum of the first `k` elements of the list `nums`
   and stores it in `current_sum`.

2. **Initialize Maximum Sum**:
   ```python
   max_sum = current_sum
   ```
   This line initializes `max_sum` with the value of `current_sum`. This will
   keep track of the maximum sum of any subarray of length `k` found so far.

3. **Sliding Window Technique**:
   ```python
   for i in range(k, len(nums)):
       current_sum += nums[i] - nums[i - k]
       max_sum = max(max_sum, current_sum)
   ```
   This loop iterates over the list starting from the `k`-th element to the
   end. In each iteration:
   - `current_sum` is updated by adding the current element `nums[i]` and
   subtracting the element that is `k` positions behind (`nums[i - k]`). This
   effectively slides the window of `k` elements one position to the right.
   - `max_sum` is updated to be the maximum of the current `max_sum` and the
   updated `current_sum`.

4. **Calculate and Return Maximum Average**:
   ```python
   return max_sum / k
   ```
   Finally, the function returns the maximum average by dividing `max_sum` by
   `k`.

This approach ensures that the function runs in O(n) time complexity, where `n`
is the length of the list `nums`, because it only requires a single pass
through the list after the initial sum calculation.

## User ───

I'm having trouble understanding line 32 currSum += nums[i] - nums[i - k].
Explain it to me using an example

## Copilot ───

Sure, let's break down the line `current_sum += nums[i] - nums[i - k]` using an
example.

Suppose we have the following list `nums` and `k` value:
```python
nums = [1, 12, -5, -6, 50, 3]
k = 4
```

### Initial Sum Calculation
First, we calculate the sum of the first `k` elements:
```python
current_sum = sum(nums[:k])  # sum([1, 12, -5, -6]) = 1 + 12 - 5 - 6 = 2
max_sum = current_sum  # max_sum = 2
```

### Sliding Window Technique
Now, we start the sliding window from the `k`-th element (index 4) to the end
of the list.

#### First Iteration (i = 4)
- `current_sum += nums[4] - nums[0]`
- `current_sum += 50 - 1`
- `current_sum = 2 + 50 - 1 = 51`

Update `max_sum`:
- `max_sum = max(max_sum, current_sum)`
- `max_sum = max(2, 51) = 51`

#### Second Iteration (i = 5)
- `current_sum += nums[5] - nums[1]`
- `current_sum += 3 - 12`
- `current_sum = 51 + 3 - 12 = 42`

Update `max_sum`:
- `max_sum = max(max_sum, current_sum)`
- `max_sum = max(51, 42) = 51`

### Explanation
The line `current_sum += nums[i] - nums[i - k]` updates the sum of the current
window by:
1. Adding the new element `nums[i]` that enters the window.
2. Subtracting the element `nums[i - k]` that exits the window.

This way, we efficiently calculate the sum of the new window without having to
sum all `k` elements from scratch.

In our example:
- When `i = 4`, the window slides from `[1, 12, -5, -6]` to `[12, -5, -6, 50]`.
- When `i = 5`, the window slides from `[12, -5, -6, 50]` to `[-5, -6, 50, 3]`.

By updating `current_sum` in this manner, we maintain the sum of the current
window and can easily find the maximum sum of any window of length `k`.

## User ───

Ok so, each iteration it looks at the next right element and adds that number
and removes the previous left element?

## Copilot ───

Yes, exactly! Each iteration of the loop looks at the next right element and
adds that number to the current sum, while simultaneously removing the previous
left element from the current sum. This effectively slides the window one
position to the right.

Here's a concise summary:
- **Add** the next right element (`nums[i]`).
- **Subtract** the previous left element (`nums[i - k]`).

This way, the sum of the current window of `k` elements is updated efficiently
without having to recalculate the sum from scratch.
"""
