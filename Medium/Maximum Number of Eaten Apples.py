from typing import List
from collections import Counter
import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ind = 0
        heap = []
        res = 0

        while heap or ind < len(apples):
            if ind < len(apples) and apples[ind] > 0:
                heapq.heappush(heap, [days[ind] + ind, apples[ind]])

            while heap and (heap[0][0] <= ind or heap[0][1] <= 0):
                heapq.heappop(heap)

            if heap:
                heap[0][1] -= 1
                res += 1

            ind += 1

        return res


if __name__ == '__main__':
    apples = [1, 2, 3, 5, 2]
    days = [3, 2, 1, 4, 2]
    print(Solution().eatenApples(apples, days))
