from math import inf
from collections import deque


class Solution:
    def shortestPathLength(self, graph):
        # 1 <= graph.length <= 12
        # 0 <= graph[i].length < graph.length

        nodeCount = len(graph)

        # conceptually masks[k] indicates that only node k has been visited
        masks = [1 << i for i in range(nodeCount)]
        # used to check whether all nodes have been visited (11111...111)
        allVisited = (1 << nodeCount) - 1
        queue = deque([(0, i, masks[i]) for i in range(nodeCount)])
        steps = 0

        # encoded_visited in visited_states[node] iff
        # (node, encoded_visited) has been pushed onto the queue
        visited_states = [{masks[i]} for i in range(nodeCount)]
        # states in visited_states will never be pushed onto queue again

        while queue:
            # number of nodes to be popped off for current steps size
            # this avoids having to store steps along with the state
            # which consumes both time and memory
            steps, currentNode, visited = queue.popleft()
            if visited == allVisited:
                return steps

            # start bfs from each neighbor
            for nb in graph[currentNode]:
                new_visited = visited | masks[nb]
                # pre-check here to for efficiency, as each steps increment may results
                # in huge # of nodes being added into queue
                if new_visited == allVisited:
                    return steps + 1
                if new_visited not in visited_states[nb]:
                    visited_states[nb].add(new_visited)
                    queue.append((steps + 1, nb, new_visited))

        # no path which explores every node
        return inf

if __name__ == '__main__':
    graph = [[1], [0, 2, 4], [1, 3], [2], [1, 5], [4]]
    print(Solution().shortestPathLength(graph))
