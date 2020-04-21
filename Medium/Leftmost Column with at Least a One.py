"""
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in
non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it.
If such index doesn't exist, return -1.
You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.
For custom testing purposes you're given the binary matrix mat as input in the following four examples.
You will not have access the binary matrix directly.

Example:
Input:
    mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output:
    1
"""


class BinaryMatrix:
    """
    Helper class implemented fo reference, not given in problem
    """
    def __init__(self, grid):
        self.grid = grid

    def get(self, x: int, y: int) -> int:
        return self.grid[x][y]

    def dimensions(self):
        x = len(self.grid)
        y = len(self.grid[0])
        return x, y


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        def binary_search(low, high, rows):
            answer = []
            while low <= high:
                mid = (low + high) // 2
                for row_index in rows:
                    if binaryMatrix.get(row_index, mid) == 1:
                        answer.append(row_index)
                if (low == high or mid == 0) and answer: # return the lowest column found
                    return mid
                if not answer:
                    low = mid + 1
                    return binary_search(low, high, rows)
                else:
                    high = mid
                    return binary_search(low, high, answer)
            return -1

        return binary_search(0, rows - 1, list(range(rows)))


if __name__ == "__main__":
    grid = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
    binary_grid = BinaryMatrix(grid)
    print(Solution().leftMostColumnWithOne(binary_grid))