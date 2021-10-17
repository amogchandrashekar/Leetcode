from typing import List
from collections import defaultdict, Counter
from functools import lru_cache


class Excel:

    def __init__(self, height: int, width: str):
        self.sheet = [[0] * (self.convert_char_to_int(width) + 1) for _ in range(height)]

    @staticmethod
    def convert_char_to_int(char):
        return ord(char) - ord('A')

    def set(self, row: int, column: str, val: int) -> None:
        row = row - 1
        column = self.convert_char_to_int(column)
        self.sheet[row][column] = val

    def get(self, row: int, column: str) -> int:
        row = row - 1
        column = self.convert_char_to_int(column)
        return self.get_val(row, column)

    def get_val(self, row: int, column: int) -> int:
        if type(self.sheet[row][column]) is int:
            return self.sheet[row][column]

        # if its a counter, then we have to sum up all the values in the cell
        ans = 0
        for (r, c), occurance in self.sheet[row][column].items():
            ans += self.get_val(r, c) * occurance
        return ans

    def get_loc(self, cell):
        letter = ''.join(char for char in cell if char.isalpha())
        numeric = ''.join(char for char in cell if char.isnumeric())
        return int(numeric) - 1, self.convert_char_to_int(letter)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cells = Counter()
        row = row - 1
        column = self.convert_char_to_int(column)

        for cell in numbers:

            if ':' not in cell:
                r, c = self.get_loc(cell)
                cells[(r, c)] += 1

            else:
                start, end = cell.split(':')
                start_r, start_c = self.get_loc(start)
                end_r, end_c = self.get_loc(end)
                for r in range(start_r, end_r + 1):
                    for c in range(start_c, end_c + 1):
                        cells[(r, c)] += 1

        self.sheet[row][column] = cells
        return self.get_val(row, column)


if __name__ == '__main__':
    excel = Excel(3, "C")
    excel.set(1, "A", 2)
    excel.sum(3, "C", ["A1", "A1:B2"])
    excel.set(2, "B", 2)
    excel.get(3, "C")
