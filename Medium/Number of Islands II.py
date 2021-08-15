"""
Definition for a point.
"""


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        class DSU(object):
            def __init__(self, length):
                self.par = list(range(length))
                self.isLand = [False] * length
                self.rank = [1] * length
                self.count = 0

            def find(self, x):
                if self.par[x] != x:
                    self.par[x] = self.find(self.par[x])
                return self.par[x]

            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                if self.rank[px] >= self.rank[py]:
                    self.par[py] = px
                    self.rank[px] += self.rank[py]
                else:
                    self.par[px] = py
                    self.rank[py] += self.rank[px]
                self.count -= 1
                return True

            def addLand(self, x):
                self.isLand[x] = True
                self.count += 1

        def index(x, y):
            return x * n + y

        dsu = DSU(m * n)
        res = list()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for p in positions:
            x, y = p.x, p.y
            dsu.addLand(index(x, y))

            for dr, dc in directions:
                dx, dy = x + dr, y + dc
                if dx in range(m) and dy in range(n) and dsu.isLand[index(dx, dy)]:
                    dsu.union(index(x, y), index(dx, dy))

            res.append(dsu.count)
        return res


if __name__ == '__main__':
    n = 8
    m = 14
    A = [[0,9],[5,4],[0,12],[6,9],[6,5],[0,4],[4,11],[0,0],[3,5],[6,7],[3,12],[0,5],[6,13],[7,5],[3,6],[4,4],[0,8],[3,1],[4,6],[6,1],[5,12],[3,8],[7,0],[2,9],[1,4],[3,0],[1,13],[2,13],[6,0],[6,4],[0,13],[0,3],[7,4],[1,8],[5,5],[5,7],[5,10],[5,3],[6,10],[6,2],[3,10],[2,7],[1,12],[5,0],[4,5],[7,13],[3,2]]
    operators = [Point(x, y) for x, y in A]
    print(Solution().numIslands2(n, m, operators))
