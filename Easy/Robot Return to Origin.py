class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0, 0]

        for move in moves:

            if move == 'R':
                position[0] += 1

            elif move == 'L':
                position[0] -= 1

            elif move == 'U':
                position[1] += 1

            else:
                position[1] -= 1

        return position == [0, 0]