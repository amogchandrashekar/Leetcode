class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        char_map = {}
        exists = set()

        for i in range(26):
            char_map[chr(ord('a') + i)] = (i // 5, i % 5)
            exists.add((i // 5, i % 5))

        start_x, start_y = 0, 0
        res = []

        for char in target:
            end_x, end_y = char_map[char]

            while start_x != end_x or start_y != end_y:

                while start_x > end_x and (start_x - 1, start_y) in exists:
                    res.append("U")
                    start_x -= 1

                while start_x < end_x and (start_x + 1, start_y) in exists:
                    res.append("D")
                    start_x += 1

                while start_y < end_y and (start_x, start_y + 1) in exists:
                    res.append("R")
                    start_y += 1

                while start_y > end_y and (start_x, start_y - 1) in exists:
                    res.append("L")
                    start_y -= 1

            res.append("!")

        return "".join(res)


if __name__ == "__main__":
    s = 'zdz'
    print(Solution().alphabetBoardPath(s))