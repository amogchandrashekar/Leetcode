"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.
"""
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = dict()

        def dfs(node, color):
            if node in colored:
                return colored[node] == color

            colored[node] = color
            return all(dfs(adj_node, 1 - color) for adj_node in graph[node])

        return all(dfs(node, 1) for node in range(len(graph)) if node not in colored)


if __name__ == '__main__':
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(Solution().isBipartite(graph))
