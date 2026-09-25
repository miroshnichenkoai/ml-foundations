"""LeetCode 217. Contains Duplicate.

https://leetcode.com/problems/contains-duplicate
Time: O(n), make set from list.
Memory: O(1).
Technique: comparison set len with dict len.
Solved: on my own.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
