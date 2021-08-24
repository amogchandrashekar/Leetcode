"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000

Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""
from functools import lru_cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        @lru_cache(maxsize=None)
        def dfs(power):
            if power == 0:
                return 1

            if power % 2 == 0:
                return dfs(power // 2) * dfs(power // 2)
            else:
                return x * dfs(power // 2) * dfs(power // 2)

        ans = dfs(abs(n))
        return ans if n > 0 else 1 / ans



if __name__ == "__main__":
    x = 34.00515
    n = -3
    print(x ** n)
    print(Solution().myPow(x, n))