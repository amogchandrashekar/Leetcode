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
        answer = list()

        def dfs(result, target, index):
            if target == 0:
                result.sort()
                if result not in answer:
                    answer.append(result)
                return
            elif target < 0:
                return
            else:
                for ind, num in enumerate(candidates[index:]):
                    dfs(result + [num], target - num, index + ind + 1)

        dfs([], target, 0)
        return answer


if __name__ == "__main__":
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(Solution().combinationSum2(candidates, target))