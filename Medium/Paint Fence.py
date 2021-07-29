class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def numWays(self, n, k):
        # write your code here

        memo = dict()

        def dfs(ind, rem, prev_num):
            if ind == n - 1:
                return 1

            if (ind, rem) in memo:
                return memo[(ind, rem)]

            ans = 0
            for i in range(k):
                if prev_num != i:
                    ans += dfs(ind + 1, 1, i)
                elif rem:
                    ans += dfs(ind + 1, rem - 1, i)
            memo[(ind, rem)] = ans

            return ans

        return dfs(-1, 1, -1)


if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution().numWays(n, k))