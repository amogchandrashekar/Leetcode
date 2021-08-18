class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos_x, pos_y = 0, 0
        dir_x, dir_y = 0, 1

        for instruction in instructions:

            if instruction == 'L':
                dir_x, dir_y = -dir_y, dir_x

            elif instruction == 'R':
                dir_x, dir_y = dir_y, -dir_x

            else:
                pos_x += dir_x
                pos_y += dir_y

        return (pos_x, pos_y) == (0, 0) or (dir_x, dir_y) != (0, 1)