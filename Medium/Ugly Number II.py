"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

import heapq


class Solution:
    def nthuglynumber(self, n: int) -> int:
        heap, ans, ans_set = [1], 1, set()
        for _ in range(n):
            while ans in ans_set: ans = heapq.heappop(heap)
            ans_set.add(ans)
            for i in [2, 3, 5]: heapq.heappush(heap,i*ans)
        return ans


if __name__=="__main__":
    n = 8
    print(Solution().nthuglynumber(n))