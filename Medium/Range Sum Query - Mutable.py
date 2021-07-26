from typing import List


class NumArray:

    def find_RSB(self, i):
        return i & -i

    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        self.n = len(self.nums)
        self.tree = [num for num in self.nums]

        for child in range(1, self.n):
            parent = child + self.find_RSB(child)
            if parent < self.n:
                self.tree[parent] += self.tree[child]

    def update(self, index: int, val: int) -> None:
        ind = index + 1
        to_add = val - self.nums[ind]
        self.nums[ind] = val

        while ind < self.n:
            self.tree[ind] += to_add
            ind += self.find_RSB(ind)

    def prefix_sum(self, ind):
        ans = 0
        while ind != 0:
            ans += self.tree[ind]
            ind -= self.find_RSB(ind)
        return ans

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum(right + 1) - self.prefix_sum(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
