from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0

        min_jump = [float("inf") for _ in nums]
        min_jump[0] = 0

        for i, num in enumerate(nums):
            for j in range(i + 1, min(num + i + 1, len(nums))):
                min_jump[j] = min(min_jump[j], 1 + min_jump[i])
                if j == len(nums) - 1:
                    return min_jump[-1]
        return min_jump[-1]


if __name__ == "__main__":
    print(Solution().jump([2,3,0,1,4]))