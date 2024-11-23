"""
Anagram Groups
Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

Notes:
    Input: 
        - Array of Strings
    Output:
         - Array of Arrays

    - An anagram is a word that contains the exact same letters as another word
    
    - Create a hashmap of the sorted word as the key and anagrams as the value
    - Iterate through the array of strings
    - Sort each word in alphabetical order
    - Put the word in the hashmap
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            anagram = "".join(sorted(word))
            anagrams[anagram] = anagrams.get(anagram, [])
            anagrams[anagram].append(word)

        return list(anagrams.values())


print(Solution().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))

