"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # find the longest identical prefix of m and n
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        return m << count


if __name__ == "__main__":
    m = 600000000
    n = 2147483645
    print(Solution().rangeBitwiseAnd(m, n))
