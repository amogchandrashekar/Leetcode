class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(ind):

            if ind >= len(s):
                return 1

            if s[ind] == '0':
                return 0

            if ind in memo:
                return memo[ind]

            max_decoding = dfs(ind + 1)
            if (ind + 1 < len(s)) and (s[ind] == '1' or s[ind] == '2' and s[ind + 1] in '0123456'):
                max_decoding += dfs(ind + 2)

            memo[ind] = max_decoding
            return max_decoding

        return dfs(0)


if __name__ == '__main__':
    s = "2611055971756562"
    print(Solution().numDecodings(s))