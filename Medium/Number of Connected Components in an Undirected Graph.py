from typing import List


class DSU:

    def __init__(self, nodes):
        self.parents = list(range(nodes))
        self.rank = [1] * nodes

    def find(self, node):
        par = self.parents[node]
        while par != self.parents[par]:
            self.parents[par] = self.parents[self.parents[par]]
            par = self.parents[par]
        return par

    def union(self, nodea, nodeb):
        para, parb = self.find(nodea), self.find(nodeb)

        if para == parb:
            return 0

        ranka, rankb = self.rank[para], self.rank[parb]
        if ranka > rankb:
            self.parents[parb] = para
        elif rankb > ranka:
            self.parents[para] = parb
        else:
            self.rank[para] += 1
            self.parents[parb] = para
        return -1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        islands = n
        dsu = DSU(n)

        for src, dst in edges:
            islands += dsu.union(src, dst)

        return islands