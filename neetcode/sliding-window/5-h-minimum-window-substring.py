"""
Minimum Window Substring
Given two strings s and t, return the shortest substring of s such that every
character in t, including duplicates, is present in the substring.
If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y",
and "Z" from string t.

Example 2:
Input: s = "xyz", t = "xyz"
Output: "xyz"

Example 3:
Input: s = "x", t = "xy"
Output: ""

Constraints:
1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, res, hash = 0, "", {}

        for c in t:
            hash[c] = True

        while l < len(s):
            if s[l] in hash:
                temp = hash.copy()

                for r in range(l, len(s)):
                    if s[r] in temp:
                        del temp[s[r]]
                    if not temp:
                        if res == "":
                            res = s[l: r + 1]
                        else:
                            res = min(s[l:r + 1], res)
                        print(res)
                        break
            l += 1

        return res


s = "OUZODYXAZV"
t = "XYZ"

print(Solution().minWindow(s, t))  # ""
