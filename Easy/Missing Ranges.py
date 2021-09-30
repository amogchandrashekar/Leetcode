from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower - 1] + nums + [upper + 1]
        ans = list()

        for ind in range(len(nums) - 1):
            cur_num = nums[ind]
            next_num = nums[ind + 1]

            low = cur_num + 1
            high = next_num - 1

            if high < low:
                continue

            elif low == high:
                ans.append(f'{low}')

            else:
                ans.append(f'{low}->{high}')

        return ans