from typing import List
from functools import lru_cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def memo(left_ind, right_ind):
            if left_ind > right_ind:
                return 0

            return max(piles[left_ind] + min(memo(left_ind + 1, right_ind - 1), memo(left_ind + 2, right_ind)),
                       piles[right_ind] + min(memo(left_ind + 1, right_ind - 1), memo(left_ind, right_ind - 2)))

        alice = memo(0, len(piles) - 1)
        return True if alice > 0 else False