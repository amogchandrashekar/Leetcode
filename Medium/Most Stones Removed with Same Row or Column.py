from typing import List
from collections import defaultdict


class DSU:

    def __init__(self, stones):
        self.parents = defaultdict(set)
        self.ranks = defaultdict(int)
        for stone in stones:
            self.parents[tuple(stone)] = tuple(stone)
            self.ranks[tuple(stone)] = 1

        self.row_set = defaultdict(list)
        self.col_set = defaultdict(list)

    def find(self, node):
        parent = self.parents[node]
        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent

    def union(self, nodea, nodeb):
        par_a, par_b = self.find(nodea), self.find(nodeb)

        if par_a == par_b:
            return

        rank_a, rank_b = self.ranks[par_a], self.ranks[par_b]

        if rank_a > rank_b:
            self.parents[par_b] = par_a
        elif rank_b > rank_a:
            self.parents[par_a] = par_b
        else:
            self.parents[par_b] = par_a
            self.ranks[par_a] += 1

    def find_similar(self, stone):
        x, y = stone

        if x in self.row_set:
            self.union(self.row_set[x][0], stone)
        if y in self.col_set:
            self.union(self.col_set[y][0], stone)

        self.row_set[x].append(stone)
        self.col_set[y].append(stone)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU(stones)
        for stone in stones:
            dsu.find_similar(tuple(stone))

        unique = set()
        for stone in stones:
            unique.add(dsu.find(tuple(stone)))

        return len(stones) - len(unique)


if __name__ == '__main__':
    stones = [[0,1],[1,0],[1,1]]
    print(Solution().removeStones(stones))
