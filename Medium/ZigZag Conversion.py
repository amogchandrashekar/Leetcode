from collections import defaultdict


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = -1
        res = defaultdict(list)
        row = 0

        for char in s:
            if row == 0 or row == numRows - 1:
                direction = -1 * direction

            res[row].append(char)
            row += direction

        return "".join("".join(res[row]) for row in sorted(res))


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))