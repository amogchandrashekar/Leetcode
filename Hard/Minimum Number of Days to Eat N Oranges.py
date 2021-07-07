class Solution:
    def minDays(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]

            memo[remaining] = 1 + min(
                (remaining % 2) + dfs(remaining // 2),
                (remaining % 3) + dfs(remaining // 3)
            )

            return memo[remaining]

        return dfs(n)


if __name__ == '__main__':
    n = 834827
    print(Solution().minDays(n))