from typing import List
from heapq import heappop, heappush


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        extra_bricks = list()

        for ind in range(len(heights) - 1):

            if heights[ind] < heights[ind + 1]:
                needed_bricks = heights[ind + 1] - heights[ind]
                bricks -= needed_bricks
                heappush(extra_bricks, -needed_bricks)

                if bricks < 0:

                    if ladders > 0:
                        ladders -= 1
                        bricks -= heappop(extra_bricks)
                    else:
                        return ind

        return len(heights) - 1


if __name__ == '__main__':
    heights = [14, 3, 19, 3]
    bricks = 17
    ladders = 2
    print(Solution().furthestBuilding(heights, bricks, ladders))
