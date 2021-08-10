from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        init_mask = (2 ** len(nums)) - 1
        ans = []

        def dfs(mask, path):
            if mask == 0:
                nonlocal ans
                ans.append(path)
                return

            for ind in range(len(nums)):
                if mask & (1 << ind):
                    dfs(mask ^ (1 << ind), path + [nums[ind]])

        dfs(init_mask, [])
        return ans


if __name__ == '__main__':
    nums = [0,1]
    print(Solution().permute(nums))
