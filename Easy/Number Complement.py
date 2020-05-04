"""
Given a positive integer, output its complement number.
The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010.
So you need to output 2.
"""


class Solution:
    def findComplement(self, num: int) -> int:
        b_str = bin(num).replace('0b', '')
        mask_str = ''.join(['1'] * len(b_str))
        return num ^ int(mask_str, 2)


if __name__ == "__main__":
    num = 3
    print(Solution().findComplement(num))