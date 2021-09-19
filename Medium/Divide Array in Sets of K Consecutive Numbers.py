from typing import List
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)

        for num in sorted(nums):
            if counter[num] == 0:
                continue

            group_size = 1
            cur_num = num
            counter[num] -= 1

            while group_size != k:
                if counter[cur_num + 1] > 0:
                    counter[cur_num + 1] -= 1
                    cur_num += 1
                    group_size += 1
                else:
                    return False

        return True


if __name__ == '__main__':
    nums = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
    k = 3
    print(Solution().isPossibleDivide(nums, k))