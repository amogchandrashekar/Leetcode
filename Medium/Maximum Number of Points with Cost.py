from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def get_pre_max(arr):
            left = [arr[0]]
            for num in arr[1:]:
                left.append(max(left[-1] - 1, num))
            return left

        for row_id in range(1, len(points)):
            prev_row_id = row_id - 1
            left = get_pre_max(points[prev_row_id])
            right = get_pre_max(points[prev_row_id][::-1])[::-1]
            for ind in range(len(points[row_id])):
                points[row_id][ind] += max(left[ind], right[ind])

        return max(points[-1])


if __name__ == '__main__':
    points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    print(Solution().maxPoints(points))
