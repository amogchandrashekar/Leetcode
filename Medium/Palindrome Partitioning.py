from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = list()

        def dfs(ind, palindromes):
            if palindromes and palindromes[-1] != palindromes[-1][::-1]:
                return

            if ind == len(s):
                nonlocal ans
                ans.append(palindromes)
                return

            for i in range(ind, len(s)):
                dfs(i + 1, palindromes + [s[ind:i + 1]])

        dfs(0, [])
        return ans