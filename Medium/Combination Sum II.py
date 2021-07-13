"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = list()

        def dfs(ind, path, rem):
            if rem == 0:
                nonlocal ans
                ans.append(path)
                return

            if rem < 0:
                return

            prev = -1
            for i in range(ind + 1, len(candidates)):
                if candidates[i] == prev:
                    continue
                dfs(i, path + [candidates[i]], rem - candidates[i])
                prev = candidates[i]

        dfs(-1, [], target)
        return ans


if __name__ == "__main__":
    candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 27
    print(Solution().combinationSum2(candidates, target))
