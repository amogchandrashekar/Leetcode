"""
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices.
You spend 1 second to walk over one edge of the tree.
Return the minimum time in seconds you have to spend in order to
collect all apples in the tree starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges,
where edges[i] = [fromi, toi] means that exists an edge connecting the vertices fromi and toi.
Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple, otherwise, it does not have any apple.
"""


from typing import List
from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for start, end in edges:
            tree[start].append(end)

        def dfs(node):
            cost = 0
            for child in tree[node]:
                cost += dfs(child)
            if cost or hasApple[node]:
                return cost + 1
            return 0

        res = dfs(0)
        return 2*(res-1) if res else 0


if __name__ == "__main__":
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    hasApple = [False, False, True, False, True, True, False]
    print(Solution().minTime(n, edges, hasApple))