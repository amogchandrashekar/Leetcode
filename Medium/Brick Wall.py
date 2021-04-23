"""
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same
height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in
this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to
draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall,
in which case the line will obviously cross no bricks.
"""
from typing import List
from itertools import accumulate
from collections import Counter


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cum_sum = list()
        for row in wall:
            row_sum = list(accumulate(row[:len(row) - 1]))
            cum_sum += row_sum
        counter = Counter(cum_sum)
        return len(wall) - max(counter.values(), default=0)


if __name__ == "__main__":
    wall = [[1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]]
    print(Solution().leastBricks(wall))
