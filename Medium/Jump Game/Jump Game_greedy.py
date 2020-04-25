from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for index in range(len(nums) - 1, -1, -1):
            last_pos = max(last_pos, index + nums[index])
        return last_pos == 0


if __name__ == "__main__":
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))