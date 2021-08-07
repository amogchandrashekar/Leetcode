from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [[0, 1], [-1, 0], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
        board[rMove][cMove] = color

        def is_valid(dir):
            x, y = dir
            dr, dc = rMove + x, cMove + y
            length = 1

            while dr in range(8) and dc in range(8):
                length += 1
                if board[dr][dc] == '.':
                    return False
                if board[dr][dc] == color:
                    return length >= 3
                dr, dc = dr + x, dc + y

            return False

        for d in directions:
            if is_valid(d):
                return True

        return False


if __name__ == '__main__':
    board = [[".", ".", "W", ".", "B", "W", "W", "B"],
             ["B", "W", ".", "W", ".", "W", "B", "B"],
             [".", "W", "B", "W", "W", ".", "W", "W"],
             ["W", "W", ".", "W", ".", ".", "B", "B"],
             ["B", "W", "B", "B", "W", "W", "B", "."],
             ["W", ".", "W", ".", "W", "B", "W", "W"],
             ["B", ".", "B", "B", ".", ".", "B", "B"],
             [".", "W", ".", "W", ".", "W", ".", "W"]]
    rMove = 5
    cMove = 4
    color = "W"
    print(Solution().checkMove(board, rMove, cMove, color))
