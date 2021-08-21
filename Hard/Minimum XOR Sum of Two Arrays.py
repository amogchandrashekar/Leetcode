from functools import lru_cache
from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dfs(ind, mask):

            if mask == 0:
                return 0

            ans = float('inf')
            num = nums1[ind]
            for i in range(len(nums2)):
                if mask & (1 << i):
                    ans = min(ans, (num ^ nums2[i]) + dfs(ind + 1, mask ^ (1 << i)))

            return ans

        all_set_mask = (2 ** len(nums1)) - 1
        return dfs(0, all_set_mask)


if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [2,3]
    print(Solution().minimumXORSum(nums1, nums2))