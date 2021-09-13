from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list = defaultdict(dict)

        for ind, (nr, dr) in enumerate(equations):
            value = values[ind]
            adj_list[nr][dr] = value
            adj_list[dr][nr] = 1 / value

        def get_cost(nr, dr):
            queue = deque([[nr, 1.0]])
            seen = set()
            seen.add(nr)

            while queue:
                node, cost = queue.popleft()

                if node == dr:
                    return cost

                for adj_node in adj_list[node]:
                    if adj_node not in seen:
                        seen.add(adj_node)
                        queue.append([adj_node, cost * adj_list[node][adj_node]])

            return -1

        answer = list()
        for nr, dr in queries:
            if nr not in adj_list or dr not in adj_list:
                answer.append(-1)
            else:
                cost = get_cost(nr, dr)
                if cost != -1:
                    adj_list[nr][dr] = cost
                    adj_list[dr][nr] = 1 / cost
                answer.append(get_cost(nr, dr))

        return answer


if __name__ == '__main__':
    equations = [["a", "b"], ["c", "d"], ["e", "f"], ["g", "h"]]
    values = [4.5, 2.3, 8.9, 0.44]
    queries = [["a", "c"], ["d", "f"], ["h", "e"], ["b", "e"], ["d", "h"], ["g", "f"], ["c", "g"]]
    print(Solution().calcEquation(equations, values, queries))
