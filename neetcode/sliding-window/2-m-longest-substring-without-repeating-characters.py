"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate
characters.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        # Dictionary to store the last occurrence index of each character
        occ = {}
        # Iterate over the string with `r` as the right pointer
        for r in range(len(s)):
            # If the character at `r` is already in the dictionary
            if s[r] in occ:
                # Move the left pointer `l` to the right of the last occurrence
                l = max(l, occ[s[r]] + 1)
            # Update the last occurrence of the character at `r`
            occ[s[r]] = r
            # Update the result with the maximum length found
            res = max(res, r - l + 1)

        return res


s = "au"
print(Solution().lengthOfLongestSubstring(s))
