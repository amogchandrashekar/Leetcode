from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length, width = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(r, c, i, seen):

            if board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            for x, y in directions:
                if r + x in range(length) and c + y in range(width) and (r + x, c + y) not in seen:
                    seen.add((r + x, c + y))
                    if dfs(r + x, c + y, i + 1, seen):
                        return True
                    seen.remove((r + x, c + y))

        for row_id in range(length):
            for col_id in range(width):
                if dfs(row_id, col_id, 0, {(row_id, col_id)}):
                    return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    print(Solution().exist(board, word))
