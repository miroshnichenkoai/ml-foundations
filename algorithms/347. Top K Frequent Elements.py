"""LeetCode 347. Top K Frequent Elements.

https://leetcode.com/problems/top-k-frequent-elements
Time: O(n).
Memory: O(n).
Technique: count most common int.
Solved: on my own.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res: list[int] = []

        for v in Counter(nums).most_common(k):
            res.append(v[0])

        return res
