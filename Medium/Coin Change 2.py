"""
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Note:
You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
"""

from typing import List


class Solution:
    def change_backtracking(self, amount: int, coins: List[int]) -> int:
        memo = dict()
        coins.sort()
        def dfs(index, remaining):
            if (index, remaining) in memo:
                return memo[(index, remaining)]
            if remaining == 0:
                return 1

            cnt = 0
            for ind in range(index, len(coins)):
                if remaining - coins[ind] >= 0:
                    cnt += dfs(ind, remaining - coins[ind])

            memo[(index, remaining)] = cnt
            return cnt

        return dfs(0, amount)

    def change_space_complexity_on2(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        for row_index in range(1, len(dp)):
            for col_index in range(len(dp[row_index])):
                if col_index == 0:
                    dp[row_index][col_index] = 1
                elif col_index - coins[row_index - 1] >= 0:
                    dp[row_index][col_index] = dp[row_index - 1][col_index] +\
                                               dp[row_index][col_index - coins[row_index - 1]]
                else:
                    dp[row_index][col_index] = dp[row_index - 1][col_index]
        return dp[-1][-1]

    def change_space_complexity_on1(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for col_index in range(coin, len(dp)):
                dp[col_index] += dp[col_index - coin]
        return dp[-1]


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change_space_complexity_on1(amount, coins))