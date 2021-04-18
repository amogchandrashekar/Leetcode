from typing import List


class Solution:
    def rob_recursive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(nums[0] + self.rob_recursive(nums[2:]), nums[1] + self.rob_recursive(nums[3:]))

    def rob_dp(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i, num in enumerate(nums[2:], start=2):
            dp[i] = max(num + dp[i - 2], dp[i - 1])
        return dp[-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 100, 234, 15, 6, 124, 98, 66, 1]
    print(Solution().rob_dp(nums))