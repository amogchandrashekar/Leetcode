from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        len_workers = len(workers)
        distances = defaultdict(dict)

        def manhattan_dist(worker, bike):
            worker_x, worker_y = worker
            bike_x, bike_y = bike
            return abs(worker_x - bike_x) + abs(worker_y - bike_y)

        for wid, worker in enumerate(workers):
            for bid, bike in enumerate(bikes):
                dist = manhattan_dist(worker, bike)
                distances[wid][bid] = dist

        @lru_cache(None)
        def assign_bikes(ind, mask):
            if ind == len_workers:
                return 0

            min_distance = float('inf')

            for bike_ind in range(len(bikes)):
                if mask & (1 << bike_ind):
                    continue

                min_distance = min(min_distance,
                                   distances[ind][bike_ind] + assign_bikes(ind + 1, mask ^ (1 << bike_ind)))

            return min_distance

        return assign_bikes(0, 0)


if __name__ == '__main__':
    workers = [[239, 904], [191, 103], [260, 117], [86, 78], [747, 62]]
    bikes = [[660, 8], [431, 772], [78, 576], [894, 481], [451, 730], [155, 28]]
    # workers = [[0, 0], [1, 1], [2, 0]]
    # bikes = [[1, 0], [2, 2], [2, 1]]
    print(Solution().assignBikes(workers, bikes))
