class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num /= x
        return num == 1

print(Solution().isUgly(-1000))
