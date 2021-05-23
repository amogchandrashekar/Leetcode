from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        start, end = 1, 10 ** 7
        max_speed = -1

        while start <= end:
            mid = (start + end) // 2
            dist_hours = [math.ceil(distance / mid) for distance in dist[:len(dist) - 1]]
            dist_hours += [dist[-1] / mid]
            dist_sum = sum(dist_hours)

            if dist_sum > hour:
                start = mid + 1
            elif dist_sum <= hour:
                end = mid - 1
                max_speed = mid

        return max_speed


if __name__ == '__main__':
    dist = [1, 3, 2]
    hour = 6
    print(Solution().minSpeedOnTime(dist, hour))