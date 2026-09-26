"""LeetCode 1. Two Sum.

https://leetcode.com/problems/two-sum
Time: O(n).
Memory: O(n).
Technique: hash map.
Solved: on my own.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d : dict[int, int] = {k: i for i, k in enumerate(nums)}

        for i, k in enumerate(nums):
            index = d.get(target - k)
            if index is not None and index != i:
                return [index, i]
        return []
