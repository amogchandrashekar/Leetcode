class Solution:

    def longestPalindrome(self, s: str) -> str:
        ans = ''
        max_len = float('-inf')
        LEN = len(s)

        def update_palindrome(l, r):
            while l in range(LEN) and r in range(LEN) and s[l] == s[r]:
                nonlocal max_len
                nonlocal ans
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    ans = s[l: r + 1]
                l -= 1
                r += 1

        for ind in range(len(s)):
            update_palindrome(ind, ind)
            update_palindrome(ind, ind + 1)

        return ans


if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))