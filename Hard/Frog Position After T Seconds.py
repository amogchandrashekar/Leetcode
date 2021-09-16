from typing import List
from collections import defaultdict, deque


class Solution:

    def get_adjacency_list(self, edges):
        neighbours = defaultdict(set)
        for src, dst in edges:
            neighbours[src].add(dst)
            neighbours[dst].add(src)
        return neighbours

    def dfs(self, leaf_node, prob, time):

        if time >= self.t:
            # check for target node only when this condition is met
            if leaf_node == self.target:  # update result only if the node is equal to target, else return
                self.res = prob
            return

        # we have already found our answer. no need to explore other paths
        if self.res != 0:
            return

        self.seen.add(leaf_node)
        neigh = self.neighbours[leaf_node] - self.seen

        if len(neigh) > 0:
            for adj_node in neigh:
                self.dfs(adj_node, (prob / len(neigh)), time + 1)
        else:  # the flow is at leaf node
            self.dfs(leaf_node, prob, self.t)

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        self.neighbours = self.get_adjacency_list(edges)
        self.seen = set()
        self.res = 0.0
        self.t, self.target = t, target
        self.dfs(1, 1.0, 0)
        return self.res


if __name__ == '__main__':
    n = 7
    edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
    t = 1
    target = 7
    print(Solution().frogPosition(n, edges, t, target))
