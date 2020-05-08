"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution:
    def numSquares_dp(self, n: int) -> int:
        perfect_squares = list()
        i = 1
        while i * i <= n:
            perfect_squares.append(i * i)
            i += 1
        MAX = float("inf")
        dp = [0] + [MAX] * n
        for ind in range(1, len(dp)):
            dp[ind] = min([dp[ind - square] if (ind - square) >= 0 else MAX for square in perfect_squares]) + 1
        return dp[-1]

    def numSquares_bfs(self, n: int) -> int:
        perfect_squares = list()
        i = 1
        while i * i <= n:
            perfect_squares.append(i * i)
            i += 1

        if n < 2:
            return n

        queue, count = {n}, 0
        while queue:
            count += 1
            temp = set()
            for num in queue:
                for square in perfect_squares:
                    if num == square:
                        return count
                    if num < square:
                        break
                    temp.add(num - square)
            queue = temp


if __name__ == "__main__":
    n = 23
    print(Solution().numSquares_dp(n))