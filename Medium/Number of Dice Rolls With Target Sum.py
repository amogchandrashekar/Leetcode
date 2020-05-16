"""
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.



Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation:
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation:
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation:
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation:
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation:
The answer must be returned modulo 10^9 + 7.


Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""

class Solution:
    def numRollsToTarget_memoization(self, d: int, f: int, target: int) -> int:
        memo = dict()

        def dfs(d, target):
            nonlocal counter
            if d == 0:
                return 1 if target == 0 else 0
            if (d, target) in memo:
                return memo[(d, target)]
            counter = 0
            for j in range(max(0, target - f), target):
                counter += dfs(d - 1, j)
            memo[(d, target)] = counter
            return counter

        counter = 0
        return dfs(d, target) % (10 ** 9 + 7)

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for i in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for row_index in range(1, len(dp)):
            for col_index in range(len(dp[row_index])):
                for face in range(1, f + 1):
                    if face <= col_index:
                        dp[row_index][col_index] += dp[row_index - 1][col_index - face]
        return dp[-1][-1] % (10 ** 9 + 7)


if __name__ == "__main__":
    d = 2
    f = 6
    target = 7
    print(Solution().numRollsToTarget(d, f, target))