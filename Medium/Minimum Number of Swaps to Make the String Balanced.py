class Solution:
    def minSwaps(self, s):
        bal, ans = 0, 0
        for symb in s:
            if symb == "[":
                bal += 1
            else:
                bal -= 1
            ans = min(bal, ans)
        return (-ans + 1) // 2


if __name__ == '__main__':
    s = "]]][[["
    print(Solution().minSwaps(s))
