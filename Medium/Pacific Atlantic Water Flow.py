from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        h, w = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        pac_seen, atl_seen = set(), set()

        for r in range(h):
            for c in range(w):
                if r == 0 or c == 0:
                    pacific.add((r, c))
                if r == h - 1 or c == w - 1:
                    atlantic.add((r, c))

        def dfs_pacific(rid, cid):
            stack = [[rid, cid]]
            pac_seen.add((rid, cid))

            while stack:
                r, c = stack.pop()
                for x, y in directions:
                    if r + x in range(h) and c + y in range(w) and (r + x, c + y) not in pac_seen and heights[r][c] <= \
                            heights[r + x][c + y]:
                        pac_seen.add((r + x, c + y))
                        stack.append((r + x, c + y))
                        pac_reachable.add((r + x, c + y))

        def dfs_atlantic(rid, cid):
            stack = [[rid, cid]]
            atl_seen.add((rid, cid))

            while stack:
                r, c = stack.pop()
                for x, y in directions:
                    if r + x in range(h) and c + y in range(w) and (r + x, c + y) not in atl_seen and heights[r][c] <= \
                            heights[r + x][c + y]:
                        atl_seen.add((r + x, c + y))
                        stack.append((r + x, c + y))
                        atl_reachable.add((r + x, c + y))

        pac_reachable, atl_reachable = set(), set()

        for row, col in pacific:
            if (row, col) not in pac_seen:
                dfs_pacific(row, col)

        for row, col in atlantic:
            if (row, col) not in atl_seen:
                dfs_atlantic(row, col)

        pacific = pacific.union(pac_reachable)
        atlantic = atlantic.union(atl_reachable)

        inter = pacific.intersection(atlantic)
        ans = [[r, c] for r, c in inter]
        ans.sort(key=lambda x:(x[0], x[1]))

        return ans


if __name__ == '__main__':
    heights = [[2,1],[1,2]]
    print(Solution().pacificAtlantic(heights))
