from typing import List
import heapq
from collections import defaultdict


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dic = defaultdict(list)
        ret = [-1] * len(rains)
        to_empty = []  # index
        full = set([])
        for day, lake in enumerate(rains):
            dic[lake].append(day)

        for i, lake in enumerate(rains):
            if lake:
                if lake in full:
                    return []
                full.add(lake)
                dic[lake].pop(0)
                if dic[lake]:
                    heapq.heappush(to_empty, dic[lake][0])
            else:
                if to_empty:
                    ret[i] = rains[heapq.heappop(to_empty)]
                    full.remove(ret[i])
                else:
                    ret[i] = 1
        return ret


if __name__ == "__main__":
    rains = [3,5,4,0,1,0,1,5,2,8,9]
    print(Solution().avoidFlood(rains))