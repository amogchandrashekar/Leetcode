from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        deque = collections.deque()
        for i in range(len(nums)):
            if deque and deque[0] <= i - k:
                deque.popleft()
            while deque and nums[deque[-1]] <= nums[i]:
                deque.pop()
            deque.append(i)
            if i >= k - 1:
                ans.append(nums[deque[0]])
        return ans


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))