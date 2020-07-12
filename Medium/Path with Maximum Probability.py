"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b]
is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end,
find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0.
Your answer will be accepted if it differs from the correct answer by at most 1e-5.
"""
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(dict)
        for i, edge in enumerate(edges):
            a, b = edge
            adj[a][b] = succProb[i]
            adj[b][a] = succProb[i]

        queue = list()
        heapq.heappush(queue, [-1, start])
        seen = set()
        while queue:
            prob, node = heapq.heappop(queue)
            if node == end:
                return -prob
            seen.add(node)
            for aj, p in adj[node].items():
                if aj not in seen:
                    heapq.heappush(queue, [prob * p, aj])
        return float(0)


if __name__ == "__main__":
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 1
    end = 2
    print(Solution().maxProbability(n, edges, succProb, start, end))