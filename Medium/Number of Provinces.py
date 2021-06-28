from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])

        parent = [node for node in range(rows)]
        rank = [1] * rows

        def find(node):
            par = parent[node]

            while par != parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]

            return par

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return 1

        connected_components = rows
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c]:
                    connected_components -= union(r, c)

        return connected_components



if __name__ == "__main__":
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(Solution().findCircleNum(isConnected))