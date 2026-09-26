"""LeetCode 347. Top K Frequent Elements.

https://leetcode.com/problems/top-k-frequent-elements
Time: O(nlogk)  .
Memory: O(n).
Technique: count most common int.
Solved: on my own.
"""

from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [v[0] for v in Counter(nums).most_common(k)]
