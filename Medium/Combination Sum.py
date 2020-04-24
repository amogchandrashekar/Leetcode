"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = list()

        def dfs(result, target):
            if target == 0:
                result.sort()
                if result not in answer:
                    answer.append(result)
                return
            elif target < 0:
                return
            else:
                for num in candidates:
                    dfs(result + [num], target - num)

        dfs([], target)
        return answer


if __name__ == "__main__":
    candidates = [8, 7, 4, 3]
    target = 11
    print(Solution().combinationSum(candidates, target))