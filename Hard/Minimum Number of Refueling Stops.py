from typing import List
from heapq import heappop, heappush


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = list()
        stations = [[0, startFuel]] + stations + [[target, 0]]
        cur_fuel = startFuel
        stops = 0

        for ind in range(1, len(stations)):
            dist_from_zero, fuel_at_tank = stations[ind]

            dist_travelled_from_last_station = dist_from_zero - stations[ind - 1][0]

            cur_fuel -= dist_travelled_from_last_station

            while cur_fuel < 0 and heap:
                cur_fuel -= heappop(heap)
                stops += 1

            if cur_fuel < 0:
                return -1

            heappush(heap, -fuel_at_tank)

        return stops


if __name__ == "__main__":
    target = 1000
    startFuel = 299
    stations = [[13, 21], [26, 115], [100, 47], [225, 99], [299, 141], [444, 198], [608, 190], [636, 157], [647, 255], [841, 123]]
    print(Solution().minRefuelStops(target, startFuel, stations))