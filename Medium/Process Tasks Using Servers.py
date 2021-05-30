from typing import List
import heapq


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        servers_heap = [[server, i] for i, server in enumerate(servers)]
        heapq.heapify(servers_heap)
        unavailable_servers = list()

        ans = list()
        t = 0

        for time, task in enumerate(tasks):
            t = max(t, time)

            if not servers_heap:
                t = unavailable_servers[0][0]

            while unavailable_servers and t >= unavailable_servers[0][0]:
                wait_time, server_weight, server_id = heapq.heappop(unavailable_servers)
                heapq.heappush(servers_heap, [server_weight, server_id])

            server_weight, server_id = heapq.heappop(servers_heap)
            ans.append(server_id)
            heapq.heappush(unavailable_servers, [t + task, server_weight, server_id])

        return ans


if __name__ == '__main__':
    servers = [31, 96, 73, 90, 15, 11, 1, 90, 72, 9, 30, 88]
    tasks = [87, 10, 3, 5, 76, 74, 38, 64, 16, 64, 93, 95, 60, 79, 54, 26, 30, 44, 64, 71]
    print(Solution().assignTasks(servers, tasks))
