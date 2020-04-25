from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(position):
            if position == len(nums) - 1:
                return True

            furthest_jump = min(position + nums[position], len(nums) - 1)
            for index in range(position + 1, furthest_jump + 1):
                if dfs(index):
                    return True
            return False

        return dfs(0)



if __name__ == "__main__":
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))