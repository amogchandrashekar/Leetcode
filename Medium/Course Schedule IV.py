"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1,
which is expressed as a pair: [1,0]

Given the total number of courses n, a list of direct prerequisite pairs and a list of queries pairs.

You should answer for each queries[i] whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.

Return a list of boolean, the answers to the given queries.

Please note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then,
course a is a prerequisite of course c.
"""

from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[b].append(a)

        def dfs(a, b):
            seen, queue = set(), [b]
            while queue:
                node = queue.pop(0)
                seen.add(node)
                if node == a:
                    return True
                if node in adj_list:
                    for child in adj_list[node]:
                        if child not in seen:
                            queue.append(child)
            return False

        ans = list()
        for a, b in queries:
            ans.append(dfs(a, b))
        return ans


if __name__ == "__main__":
    n = 2
    prerequisites = []
    queries = [[0, 1], [1, 0]]
    print(Solution().checkIfPrerequisite(n, prerequisites, queries))
