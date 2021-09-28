from typing import List


class DSU:

    def __init__(self, size):
        self.islands = 0
        self.parents = list(range(size))
        self.rank = [1] * size

    def find(self, node):
        par = self.parents[node]
        while self.parents[par] != par:
            self.parents[par] = self.parents[self.parents[par]]
            par = self.parents[par]
        return par

    def union(self, node_a, node_b):
        par_a, par_b = self.find(node_a), self.find(node_b)

        if par_a == par_b:
            return 0

        rank_a, rank_b = self.rank[par_a], self.rank[par_b]
        if rank_a > rank_b:
            self.parents[par_b] = par_a
        elif rank_b > rank_a:
            self.parents[par_a] = par_b
        else:
            self.parents[par_b] = par_a
            self.rank[par_a] += 1

        return -1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        dsu = DSU(m * n)
        seen = set()
        ans = list()

        for r, c in positions:
            if (r, c) in seen:
                ans.append(dsu.islands)
            else:
                islands = 1
                seen.add((r, c))

                for dx, dy in directions:
                    dr, dc = r + dx, c + dy
                    if (dr, dc) in seen:
                        islands += dsu.union(r * n + c, dr * n + dc)

                dsu.islands += islands
                ans.append(dsu.islands)

        return ans


if __name__ == '__main__':
    m = 3
    n = 3
    positions = [[0, 0], [0, 1], [1, 2], [1, 2]]
    print(Solution().numIslands2(m, n, positions))