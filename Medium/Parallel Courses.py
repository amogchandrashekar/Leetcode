from typing import List
from collections import defaultdict


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        in_degree = {(node + 1): 0 for node in range(n)}
        adj_set = defaultdict(set)

        for pre_req, subject in relations:
            if subject in adj_set[pre_req]:
                continue

            adj_set[pre_req].add(subject)
            print(in_degree)
            in_degree[subject] += 1

        queue = [node for node, indeg in in_degree.items() if indeg == 0]
        ans = 0
        all_nodes = 0

        while queue:
            next_level = list()
            ans += 1

            for node in queue:
                all_nodes += 1
                for adj_node in adj_set[node]:
                    in_degree[adj_node] -= 1
                    if in_degree[adj_node] == 0:
                        next_level.append(adj_node)
            queue = next_level

        return ans if all_nodes == n else -1