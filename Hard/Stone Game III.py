from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = dict()

        def dfs(ind):
            if ind in memo:
                return memo[ind]

            if ind >= len(stoneValue):
                return 0

            memo[ind] = float('-inf')
            for end_ind in range(ind + 1, ind + 4):
                memo[ind] = max(memo[ind], sum(stoneValue[ind:end_ind]) - dfs(end_ind))

            return memo[ind]

        max_alice = dfs(0)
        return 'Tie' if max_alice == 0 else 'Alice' if max_alice > 0 else 'Bob'


if __name__ == '__main__':
    values = [9, -4, 0, 12, -5, -13, 15, 6, -16, 8, 2, 16, 12, -6, 13, 0, -16, -11, 9, -14, 7, -1, 14]
    print(Solution().stoneGameIII(values))
