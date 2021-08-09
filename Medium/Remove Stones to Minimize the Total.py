from typing import List
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-x for x in piles]
        heapify(pq)
        for _ in range(k):
            heapq.heapreplace(pq, pq[0]//2)
        return -sum(pq)


if __name__ == '__main__':
    piles = [5, 4, 9]
    k = 2
    print(Solution().minStoneSum(piles, k))
