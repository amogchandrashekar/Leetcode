from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = dict()

        def dfs(ind, m):

            if (ind, m) in memo:
                return memo[(ind, m)]

            if ind >= len(piles):
                return 0

            cur_player_val = 0
            total_sum = sum(piles[ind:])

            for x in range(1, (2 * m) + 1):
                opponent_val = dfs(ind + x, max(x, m))
                cur_player_val = max(cur_player_val, total_sum - opponent_val)

            memo[(ind, m)] = cur_player_val
            return cur_player_val

        return dfs(0, 1)


if __name__ == '__main__':
    piles = [1, 2, 3, 4, 5, 100]
    print(Solution().stoneGameII(piles))
