from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for num in range(1, len(dp)):
            if num == 2 * offset:
                offset = 2 * offset
            dp[num] = 1 + dp[num - offset]

        return dp


if __name__ == '__main__':
    n = 2
    print(Solution().countBits(n))