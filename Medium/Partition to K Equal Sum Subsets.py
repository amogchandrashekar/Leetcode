from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or sum(nums) % k != 0:
            return False
        N = len(nums)
        nums.sort(reverse=True)

        # lets set all bits to 1 initially
        init_mask = (2 ** N) - 1
        memo = dict()

        def dfs(mask, target):

            if mask == 0:
                return target == 0

            if target == 0:
                # one pair is found, so reset target and do dfs again
                return dfs(mask, sum(nums) // k)

            if (mask, target) in memo:
                return memo[(mask, target)]

            res = False
            for ind in range(N):
                if mask & (1 << ind):
                    if target - nums[ind] >= 0:
                       if dfs(mask ^ (1 << ind), target - nums[ind]):
                           res = True
                           break

            memo[(mask, target)] = res
            return res

        return dfs(init_mask, sum(nums) // k)


if __name__ == '__main__':
    nums = [4, 2, 2]
    k = 2
    print(Solution().canPartitionKSubsets(nums, k))
