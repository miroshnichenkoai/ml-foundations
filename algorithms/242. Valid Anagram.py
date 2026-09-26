"""LeetCode 242. Valid Anagram.

https://leetcode.com/problems/valid-anagram
Time: O(n).
Memory: O(1).
Technique: memorizing appearing chars and count them in comparison str.
Solved: on my own.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d: dict[str, int] = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch in t:
            d[ch] = d.get(ch, 0) - 1
            if d[ch] < 0:
                return False

        return all(d.get(v, 0) == 0 for v in d)
