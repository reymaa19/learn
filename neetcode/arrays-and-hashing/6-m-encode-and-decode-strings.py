"""
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["leet","code","love","you"]
Output:["leet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

Notes: 
    Input: 
        - An Array of Strings
    Output:
        - The Array of Strings in its original format

    - Turn an array of strings into one single string
    - Turn the one single string back to an array of strings

    - For each string in the input list:
        - Take the length of the string
        - Concatenate a "#" delimiter
        - Concatenate the actual string to the result string

    - For decoding, use two pointer (i and j):
        - Find the length of the string using the number before the delimiter
        - Parse the length into an integer
        - Extract the word using the length and current index
        - Append the word to the result list
        - Move the current index to the next word
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


print("encode:", Solution().encode(["leet", "code", "love", "you"]))
print("decode:", Solution().decode(Solution().encode(["leet", "code", "love", "you"])))
