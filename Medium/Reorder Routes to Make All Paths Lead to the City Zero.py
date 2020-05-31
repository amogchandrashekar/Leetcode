"""
There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different
cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction
because they are too narrow.

Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0.
Return the minimum number of edges changed.

It's guaranteed that each city can reach the city 0 after reorder.
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbours = defaultdict(list)
        for source, destination in connections:
            neighbours[source].append(destination)
            neighbours[destination].append(source)

        edges = {(a, b) for a, b in connections}
        visited = set()

        reverse_edges = 0
        queue = deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for adj_node in neighbours[node]:
                if adj_node not in visited:
                    if (adj_node, node) not in edges:
                        reverse_edges += 1
                    queue.append(adj_node)
        return reverse_edges


if __name__ == "__main__":
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    print(Solution().minReorder(n, connections))
