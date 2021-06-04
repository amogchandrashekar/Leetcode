from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        depth, q = -1, deque([["0000", 0]])
        deadends = set(deadends)
        deadends.add("0000")

        while q:
            node, level = q.popleft()

            for movement in [-1, 1]:
                for i in range(4):
                    new_node = node[:i] + str((int(node[i]) + movement) % 10) + node[i + 1:]

                    if new_node == target or new_node == target:
                        return level + 1
                    if new_node not in deadends:
                        deadends.add(new_node)
                        q.append([new_node, level + 1])

        return -1


if __name__ == '__main__':
    deadends = ["0000"]
    target = "8888"
    print(Solution().openLock(deadends, target))
