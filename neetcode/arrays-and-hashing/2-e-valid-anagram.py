"""
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of
each other, otherwise return false.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.

Notes:
    Input:
        - String s, String t
    Output:
        - True, if both string contain the same characters as one another
        - False, if they do not contain the same characters as one another

    - Need to keep track of the number of occurances of each character
    - Use a hashmap
    - Loop once
    - If one string is longer than the other return False
    - If hashmaps contain the same keys and values return True
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False

        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1

        return hashS == hashT


print("valid anagram: ", Solution().isAnagram("test", "sett"))
print("invalid anagram:", Solution().isAnagram("tests", "settt"))
print("expected false:", Solution().isAnagram("aabbbb", "aaaabb"))
