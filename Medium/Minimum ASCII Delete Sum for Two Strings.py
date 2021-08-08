from functools import lru_cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        def calculate_ascii_sum(string_txt, ind):
            ascii_sum = 0
            for char in string_txt[ind:]:
                ascii_sum += ord(char)
            return ascii_sum

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return 0

            if i == len(s1):
                return calculate_ascii_sum(s2, j)

            if j == len(s2):
                return calculate_ascii_sum(s1, i)

            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(ord(s1[i]) + dfs(i + 1, j), ord(s2[j]) + dfs(i, j + 1))

        return dfs(0, 0)
