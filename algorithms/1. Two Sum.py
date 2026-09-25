"""LeetCode 1. Two Sum.

https://leetcode.com/problems/two-sum
Time: O(n^2).
Memory: O(1).
Technique: iteration through two lists.
Solved: on my own.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
