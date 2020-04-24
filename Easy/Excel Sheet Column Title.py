"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""


class Solution:
    def convertToTitle(self, num: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while num > 0:
            result.append(capitals[(num - 1) % 26])
            num = (num - 1) // 26
        result.reverse()
        return ''.join(result)


if __name__ == "__main__":
    print(Solution().convertToTitle(701))