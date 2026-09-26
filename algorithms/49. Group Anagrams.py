"""LeetCode 49. Group Anagrams.

https://leetcode.com/problems/group-anagrams
Time: O(n klogk), go through every element and sort string
Memory: O(n), only two indices.
Technique: memorizing of sorted str with its index in other list.
Solved: on my own.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        max_n: int = 0
        b: dict[str, int] = {}
        res: list[list[str]] = []
        for st in strs:
            s = "".join(sorted(st))
            index = b.get(s)
            if index is not None:
                res[index].append(st)
            else:
                b[s] = max_n
                max_n += 1
                res.append([st])
        return res
