from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1 for _ in nums]
        memo[-1] = True

        for index in range(len(nums) - 2, -1, -1):
            furthest_jump = min(index + nums[index], len(nums) - 1)
            for ind in range(index + 1, furthest_jump + 1):
                if memo[ind] is True:
                    memo[index] = True
                    break

        return memo[0] is True


if __name__ == "__main__":
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))
