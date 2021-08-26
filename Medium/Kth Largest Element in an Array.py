from typing import List
import random


class Solution:
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        larger = [x for x in nums if x > pivot]
        equal = [x for x in nums if x == pivot]
        smaller = [x for x in nums if x < pivot]

        L, M = len(larger), len(equal)

        if k <= L:
            return self.findKthLargest(larger, k)
        elif k > L + M:
            return self.findKthLargest(smaller, k - L - M)
        else:
            return equal[0]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))