from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = defaultdict(dict)

        def union(edge_a, edge_b):
            parent_a = find(edge_a)
            parent_b = find(edge_b)

            if parent_a != parent_b:
                parent[parent_b] = parent_a

        def find(edge):
            while edge in parent:
                if parent[edge] in parent:
                    parent[edge] = parent[parent[edge]]
                edge = parent[edge]
            return edge

        for a, b in edges:
            if find(a) != find(b):
                union(a, b)
            else:
                return [a, b]


if __name__ == '__main__':
    edges = [[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]
    print(Solution().findRedundantConnection(edges))
