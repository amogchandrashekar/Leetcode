from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([start_time, process_time, ind] for ind, (start_time, process_time) in enumerate(tasks))
        ind = 0
        cpu_endtime = tasks[0][0]

        heap = []
        ans = []

        while heap or ind < len(tasks):
            while ind < len(tasks) and tasks[ind][0] <= cpu_endtime:
                heapq.heappush(heap, [tasks[ind][1], tasks[ind][2]])
                ind += 1

            if heap:
                t, scheduled_task = heapq.heappop(heap)
                cpu_endtime += t
                ans.append(scheduled_task)
            else:
                cpu_endtime = tasks[ind][0]

        return ans


if __name__ == "__main__":
    tasks = [[46, 9], [46, 42], [30, 46], [30, 13], [30, 24], [30, 5], [30, 21], [29, 46], [29, 41], [29, 18], [29, 16],
             [29, 17], [29, 5], [22, 15], [22, 13], [22, 25], [22, 49], [22, 44]]
    print(Solution().getOrder(tasks))
