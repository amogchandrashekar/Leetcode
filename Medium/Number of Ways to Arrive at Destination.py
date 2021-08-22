from typing import List, Optional
from collections import defaultdict, Counter, deque
import heapq
from functools import lru_cache


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = (10 ** 9) + 7
        adj_list = defaultdict(dict)

        for edgea, edgeb, cost in roads:
            adj_list[edgea][edgeb] = cost
            adj_list[edgeb][edgea] = cost

        def dijstra():
            heap = [[0, 0]]
            dist = [float('inf')] * n
            ways = [0] * n
            dist[0] = 0
            ways[0] = 1

            while heap:
                curr_dist, node = heapq.heappop(heap)

                if curr_dist > dist[node]:
                    continue

                for adj_node, cost in adj_list[node].items():
                    new_dist = curr_dist + cost

                    if new_dist == dist[adj_node]:
                        # found another way to reach this node with same cost
                        ways[adj_node] = ways[adj_node] + ways[node]

                    elif new_dist < dist[adj_node]:
                        heapq.heappush(heap, [new_dist, adj_node])
                        ways[adj_node] = ways[node]
                        dist[adj_node] = new_dist

            return ways[-1]

        return dijstra() % MOD


if __name__ == "__main__":
    # n = 12
    # roads = [[1, 0, 2348], [2, 1, 2852], [2, 0, 5200], [3, 1, 12480], [2, 3, 9628], [4, 3, 7367], [4, 0, 22195],
    #          [5, 4, 5668],
    #          [1, 5, 25515], [0, 5, 27863], [6, 5, 836], [6, 0, 28699], [2, 6, 23499], [6, 3, 13871], [1, 6, 26351],
    #          [5, 7, 6229], [2, 7, 28892], [1, 7, 31744], [3, 7, 19264], [6, 7, 5393], [2, 8, 31998], [8, 7, 3106],
    #          [3, 8, 22370], [8, 4, 15003], [8, 6, 8499], [8, 5, 9335], [8, 9, 5258], [9, 2, 37256], [3, 9, 27628],
    #          [7, 9, 8364],
    #          [1, 9, 40108], [9, 5, 14593], [2, 10, 45922], [5, 10, 23259], [9, 10, 8666], [10, 0, 51122],
    #          [10, 3, 36294],
    #          [10, 4, 28927], [11, 4, 25190], [11, 9, 4929], [11, 8, 10187], [11, 6, 18686], [2, 11, 42185],
    #          [11, 3, 32557],
    #          [1, 11, 45037]]
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5],
                    [4, 6, 2]]
    print(Solution().countPaths(n, roads))
