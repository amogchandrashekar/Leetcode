from typing import List
from collections import defaultdict
import math


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        for src, dst, cost in edges:
            dist[src][dst] = cost
            dist[dst][src] = cost
        for node in range(n):
            dist[node][node] = 0

        for node in range(n):
            for cur_node in range(n):
                for adj_node in range(n):
                    if cur_node == node or adj_node == node:
                        continue
                    dist[cur_node][adj_node] = min(dist[cur_node][adj_node],
                                                   dist[cur_node][node] + dist[node][adj_node])

        dist_list = defaultdict(list)
        for node in range(n):
            for adj_node in range(n):
                if dist[node][adj_node] <= distanceThreshold:
                    dist_list[node].append(adj_node)

        dist_list = [[node, neighbours] for node, neighbours in dist_list.items()]
        dist_list.sort(key=lambda x: [len(x[1]), -x[0]])
        return dist_list[0][0]


if __name__ == '__main__':
    n = 6
    edges = [[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]]
    distanceThreshold = 417
    print(Solution().findTheCity(n, edges, distanceThreshold))
