from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        ans = []
        counter = defaultdict(int)

        for a, b in prerequisites:
            adj_list[b].append(a)
            counter[a] += 1
            counter[b] += 0

        seen = set()
        heap = list()

        for node, in_node in counter.items():
            heapq.heappush(heap, [in_node, node])

        while heap:
            dependency, node = heapq.heappop(heap)

            if node in seen:
                continue
            if dependency != 0:
                return list()

            seen.add(node)
            ans.append(node)
            for dependent_node in adj_list[node]:
                counter[dependent_node] -= 1
                heapq.heappush(heap, [counter[dependent_node], dependent_node])

        if len(ans) != numCourses:
            for node in range(numCourses):
                if node not in seen:
                    ans.append(node)

        return ans


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    print(Solution().findOrder(numCourses, prerequisites))
