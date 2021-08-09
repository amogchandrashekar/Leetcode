from typing import List
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        lis = list()

        for idx, num in enumerate(nums):
            if not lis or lis[-1] <= num:
                lis.append(num)
                nums[idx] = len(lis)
            else:
                ind = bisect.bisect_right(lis, num)
                lis[ind] = num
                nums[idx] = ind + 1

        return nums


if __name__ == '__main__':
    obstacles = [3, 1, 5, 6, 4, 2]
    print(Solution().longestObstacleCourseAtEachPosition(obstacles))
