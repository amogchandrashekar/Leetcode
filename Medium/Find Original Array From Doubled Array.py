from typing import List
from collections import deque


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        arr = sorted(changed)
        dq = deque([])
        res = []

        for i in arr:
            if dq and i == dq[0]:
                dq.popleft()
            else:
                dq.append(2 * i)
                res.append(i)

        return res if not dq else []


if __name__ == '__main__':
    nums = [0, 3, 2, 4, 6, 0]
    print(Solution().findOriginalArray(nums))
