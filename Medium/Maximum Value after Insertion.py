class Solution:
    def maxValue(self, n: str, x: int) -> str:
        length = len(n)
        if int(n) > 0:
            i = 0
            while i < length:
                if int(n[i]) < x:
                    return n[:i] + str(x) + n[i:]
                i += 1
            return n + str(x)

        else:
            i = 1
            while i < length:
                if int(n[i]) > x:
                    return n[:i] + str(x) + n[i:]
                i += 1
            return n + str(x)


if __name__ == '__main__':
    n = "99"
    x = 9
    print(Solution().maxValue(n, x))