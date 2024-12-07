"""
Car Fleet
There are n cars traveling to the same destination on a one-lane highway.
You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car
and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same
speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the
destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:
Input: target = 10, position = [1,4], speed = [3,2]
Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet,
meeting each other at 10, the destination.

Example 2:
Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10.
The cars starting at 1 and 0 never catch up to the car ahead of them.
Thus, there are 3 car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length.
1 <= n <= 1000
0 < target <= 1000
0 < speed[i] <= 100
0 <= position[i] < target
All the values of position are unique.

Notes:
    Input:
        - target destination (max)
        - position of each car from destination (0-destination)
        - speed of each car (iteration increase)
    Output:
        - The number of different car fleets that arrive at the destination
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine the position and speed into a list of tuples and sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)

        # Stack to keep track of the fleets
        stack = []

        # Iterate over each car
        for pos, spd in cars:
            # Calculate the time it takes for the car to reach the target
            time_to_target = (target - pos) / spd

            # If the stack is empty or the current car takes longer to reach the target than the car in front,
            # add the car to stack of car fleets
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)

        # The number of fleets is the size of the stack
        return len(stack)


target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]

print(Solution().carFleet(target, position, speed))  # 1
