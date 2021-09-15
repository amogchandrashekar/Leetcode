from typing import List
from collections import Counter


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        sorted_list = list()
        for ind, row in enumerate(nums):
            for num in row:
                sorted_list.append([num, ind])
        sorted_list.sort(key=lambda x: x[0])

        counter = Counter()
        i, j = 0, 0
        left, right = None, None
        cur_min = float('inf')

        while j < len(sorted_list):
            num, ind = sorted_list[j]
            counter[ind] += 1
            while len(counter) == len(nums):
                left_bound, ind = sorted_list[i]
                if num - left_bound < cur_min:
                    cur_min = num - left_bound
                    left = left_bound
                    right = num
                i += 1
                counter[ind] -= 1
                if counter[ind] == 0:
                    counter.pop(ind)
            j += 1

        return [left, right]


if __name__ == '__main__':
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(Solution().smallestRange(nums))
