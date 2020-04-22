"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

from typing import List
from collections import Counter


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = list()

        def dfs(balanced):
            if Counter(balanced)["("] == n + 1:
                return
            if len(balanced) == 2 * n:
                answer.append(balanced)
                return
            for bracket in ["(", ")"]:
                if Counter(balanced)["("] >= Counter(balanced)[")"]:
                    dfs(balanced + [bracket])

        dfs([])
        return ["".join(bracket) for bracket in answer]


if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))