from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        sorted_points = sorted(points, key=lambda x: x[1])   # sort points based on their end
        arrows = 1                                           # even though one segment is present, 1 should be returned
        segment = sorted_points[0]

        for point in sorted_points:
            if segment[1] < point[0]:                        # If new point is not in current segment, update segment
                arrows += 1
                segment = point
        return arrows


if __name__ == "__main__":
    points = [[2, 3], [2, 3]]
    print(Solution().findMinArrowShots(points))