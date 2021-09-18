from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        curr_range_start = None
        curr_range_end = None

        ans = list()
        for num in nums:
            if curr_range_end is not None and num == curr_range_end + 1:
                curr_range_end += 1
            else:
                if curr_range_start is not None:
                    if curr_range_end - curr_range_start == 0:
                        ans.append(str(curr_range_end))
                    else:
                        ans.append(f'{curr_range_start}->{curr_range_end}')

                curr_range_start = num
                curr_range_end = num

        if curr_range_start is None:
            return ans

        if curr_range_end - curr_range_start == 0:
            ans.append(str(curr_range_end))
        else:
            ans.append(f'{curr_range_start}->{curr_range_end}')

        return ans

