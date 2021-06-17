"""
You are given a network of n nodes, labeled from 1 to n. You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
 and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.
"""


from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        max_delay = 0
        adj_list = defaultdict(dict)

        for a, b, weight in times:
            adj_list[a][b] = weight

        queue = [[0, k]]
        seen = set()

        while queue:
            weight, node = heapq.heappop(queue)

            if node not in seen:
                seen.add(node)
                max_delay = max(max_delay, weight)

                for adj_node, delay in adj_list[node].items():
                    heapq.heappush(queue, [delay + weight, adj_node])

        return max_delay if max_delay and len(seen) == n else -1


if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(Solution().networkDelayTime(times, n, k))