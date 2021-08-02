from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(maxsize=None)
        def dfs(ind_s, ind_p):

            if ind_s == len(s) and ind_p == len(p):
                return True

            if ind_p >= len(p):
                return False

            match = (ind_s < len(s)) and (s[ind_s] == p[ind_p] or p[ind_p] == '.')

            if (ind_p + 1 < len(p)) and p[ind_p + 1] == '*':
                return dfs(ind_s, ind_p + 2) or (match and dfs(ind_s + 1, ind_p))
            if match:
                return dfs(ind_s + 1, ind_p + 1)

            return False

        return dfs(0, 0)