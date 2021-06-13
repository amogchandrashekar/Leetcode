from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum = sum(chalk)
        k = k % chalk_sum

        for i, c in enumerate(chalk):
            k = k - c
            if k < 0:
                return i


if __name__ == "__main__":
    chalk = [3, 1, 4, 2]
    k = 25
    print(Solution().chalkReplacer(chalk, k))