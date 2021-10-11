from typing import List
from random import randint


class Solution:
    def __init__(self, nums: List[int]):
        self.backup = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.backup.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = randint(i, n-1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums