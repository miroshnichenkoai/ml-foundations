"""LeetCode 242. Valid Anagram.

https://leetcode.com/problems/valid-anagram
Time: O(n).
Memory: O(n).
Technique: memorizing appearing chars and count them in comparison str.
Solved: on my own.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch in t:
            d[ch] = d.get(ch, 0) - 1
            if d[ch] < 0:
                return False

        for v in d:
            if d.get(v, 0) != 0:
                return False

        return True
