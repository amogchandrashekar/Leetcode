from typing import List
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        def inverse(num):
            return -1 * num

        task_counts = Counter(tasks)
        current_time = 0
        current_heap = list()
        for char, occurance in task_counts.items():
            heapq.heappush(current_heap, [inverse(occurance), char])

        while current_heap:
            index, next_tasks = 0, list()

            while index <= n:
                current_time += 1

                if current_heap:
                    occurance, char = heapq.heappop(current_heap)
                    if occurance + 1 != 0:
                        next_tasks.append([occurance + 1, char])

                if not current_heap and not next_tasks:
                    break

                if not current_heap:
                    current_time += n - index
                    index = n

                index += 1

            for occurance, char in next_tasks:
                heapq.heappush(current_heap, [occurance, char])

        return current_time


if __name__ == '__main__':
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    print(Solution().leastInterval(tasks, n))