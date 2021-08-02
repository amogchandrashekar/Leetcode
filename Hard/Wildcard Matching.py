class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = dict()

        def dfs(ind_s, ind_p):
            if ind_s == len(s) and ind_p == len(p):
                return True

            if ind_s >= len(s) and ind_p < len(p):
                for i in range(ind_p, len(p)):
                    if p[i] != '*':
                        return False
                return True

            if ind_p >= len(p):
                return False

            if (ind_s, ind_p) in memo:
                return memo[(ind_s, ind_p)]

            ans = False
            if p[ind_p] == '*':
                ans = ans or dfs(ind_s + 1, ind_p + 1) or dfs(ind_s + 1, ind_p) or dfs(ind_s, ind_p + 1)
            elif (p[ind_p] == '?') or (s[ind_s] == p[ind_p]):
                ans = ans or dfs(ind_s + 1, ind_p + 1)
            memo[(ind_s, ind_p)] = ans

            return ans

        return dfs(0, 0)


if __name__ == '__main__':
    s = "adceb"
    p = "*a*b"
    print(Solution().isMatch(s, p))