from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1 for _ in nums]
        memo[-1] = True

        def dfs(position):
            if memo[position] != -1:
                return memo[position]

            furthest_jump = min(position + nums[position], len(nums) - 1)
            for index in range(position + 1, furthest_jump + 1):
                if dfs(index):
                    memo[position] = True
                    return True

            memo[position] = False
            return False

        return dfs(0)


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))
