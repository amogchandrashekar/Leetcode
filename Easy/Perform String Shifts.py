from typing import List


def get_shift(shift_amount, s):
    """
    Handle cases when the shift exceeds the length of the string
    """
    if shift_amount < 0:
        a = - shift_amount
        while a >= len(s):
            a -= len(s)
        shift_amount = len(s) - a
    else:
        while shift_amount > len(s):
            shift_amount -= len(s)
    return shift_amount


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        """
        Calculate net shift, ie left shift cancels the right shift, hence calculate net shift and change
        """
        shift_amount = 0
        for direction, amount in shift:
            if direction == 0:
                shift_amount += amount
            else:
                shift_amount -= amount
        shift_amount = get_shift(shift_amount, s)
        return s[shift_amount:] + s[:shift_amount]


if __name__ == "__main__":
    s = "xqgwkiqpif"
    shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
    print(Solution().stringShift(s, shift))