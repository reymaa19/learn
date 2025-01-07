"""
Permutation in String
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise.
That means if a permutation of s1 exists as a substring of s2 then return true.

Both strings only contain lowercase letters.

Example 1:
Input: s1 = "abc", s2 = "lecabee"
Output: true
Explanation: The substring "cab" is a permutation
of "abc" and is present in "lecabee".

Example 2:
Input: s1 = "abc", s2 = "lecaabee"
Output: false

Constraints:
1 <= s1.length, s2.length <= 1000
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        perm = {}

        for c in s1:
            perm[c] = perm.get(c, 0) + 1

        temp = perm.copy()

        while r < len(s2):
            if s2[r] not in temp:
                l += 1
                r = l
                temp = perm.copy()
                continue

            if s2[r] in temp:
                temp[s2[r]] -= 1
                if temp[s2[r]] == 0:
                    del temp[s2[r]]
            if not temp:
                return True
            r += 1

        return False


s1 = "a"
s2 = "ab"

print(Solution().checkInclusion(s1, s2))
