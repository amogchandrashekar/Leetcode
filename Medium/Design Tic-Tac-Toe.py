from collections import Counter, defaultdict


class TicTacToe:

    def __init__(self, n: int):
        self.rows = defaultdict(Counter)
        self.cols = defaultdict(Counter)
        self.left_diagonal = defaultdict(Counter)
        self.right_diagonal = defaultdict(Counter)
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row][player] += 1
        self.cols[col][player] += 1
        self.left_diagonal[col - row][player] += 1
        self.right_diagonal[col + row][player] += 1

        if self.rows[row][player] == self.n or self.cols[col][player] == self.n or self.left_diagonal[col - row][
            player] == self.n or self.right_diagonal[col + row][player] == self.n:
            return player
        return 0