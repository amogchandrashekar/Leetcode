# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, (2 ** 31) - 1

        while l <= r:
            mid = (l + r) // 2
            guessed_num = guess(mid)

            if guessed_num == -1:
                r = mid - 1
            elif guessed_num == 1:
                l = mid + 1
            else:
                return mid