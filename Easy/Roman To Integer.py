class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        hmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = hmap[s[-1]]
        for i in range(len(s)-2, -1, -1):
            a=i
            if hmap[s[i]] < hmap[s[i+1]]:
                ans -= hmap[s[i]]
            else:
                ans += hmap[s[i]]
        return ans

