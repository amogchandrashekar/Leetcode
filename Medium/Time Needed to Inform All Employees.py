from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for ind, parent in enumerate(manager):
            children[parent].append(ind)

        stack = [[headID, 0]]
        max_dist = 0

        while stack:
            node, dist = stack.pop()
            max_dist = max(max_dist, dist)
            inform_time = informTime[node]
            for child in children[node]:
                stack.append([child, dist + inform_time])

        return max_dist