"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float("inf")
        dp = [0] + [MAX] * amount

        for ind in range(1, amount + 1):
            dp[ind] = min([dp[ind - coin] if ind - coin >= 0 else MAX for coin in coins]) + 1

        if dp[amount] != MAX:
            return dp[amount]
        return -1

    def coin_change_dfs(self, coins, amount):
        memo = dict()

        def dfs(rem):
            if rem in memo:
                return memo[rem]

            if rem < 0:
                return float("inf")

            if rem == 0:
                return 0

            memo[rem] = 1 + min([dfs(rem - coin) for coin in coins])
            return memo[rem]

        ans = dfs(amount)
        return ans if ans != float("inf") else -1


if __name__ == "__main__":
    coins = [1]
    amount = 1
    print(Solution().coin_change_dfs(coins, amount))