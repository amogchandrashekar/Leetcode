from typing import List
from collections import defaultdict, deque
import heapq


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        jumps = defaultdict(set)
        for ind, val in enumerate(arr):
            jumps[val].add(ind)

        queue = deque([[0, 0]])
        seen = set()
        seen.add(0)

        while queue:
            dist, ind = queue.popleft()

            if ind == len(arr) - 1:
                return dist

            neighbours = jumps[arr[ind]] | {ind + 1, ind - 1} - seen

            for index in neighbours:
                if index not in range(len(arr)):
                    continue
                if index == len(arr) - 1:
                    return dist + 1

                queue.append([dist + 1, index])
                seen.add(index)

            jumps[arr[ind]] = set()


if __name__ == '__main__':
    arr = [5, 11]
    print(Solution().minJumps(arr))
