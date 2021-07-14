from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        ans = []

        while top <= bottom and left <= right:
            # Walk top fence
            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            top += 1

            # Walk right fence
            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1

            '''
            If center is a horizontal line, prevent the bottom from rereading what the
            top row already read.
            '''
            if top <= bottom:
                # Walk bottom fence
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])
                bottom -= 1

            '''
            If center is a vertical line, prevent the left from rereading what the right
            col already read.
            '''
            if left <= right:
                # Walk left fence
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])
                left += 1

        return ans



if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))