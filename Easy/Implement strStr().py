class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, h = len(needle), len(haystack)
        i, j, nxt = 1, 0, [-1] + [0] * n
        while i < n:  # calculate next array
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                nxt[i] = j
            else:
                j = nxt[j]

        i = j = 0
        while i < h and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = nxt[j]

        return i - j if j == n else -1


if __name__ == '__main__':
    haystack = "abababd"
    needle = "ababd"
    print(Solution().strStr(haystack, needle))