class Solution:
    def lengthOfLongestSubstring(self, s):
        start_index, maxlen = 0, 0
        hashdict = dict()
        for index, alphabet in enumerate(s):
            if alphabet in hashdict and start_index <= hashdict[alphabet]:
                start_index = hashdict[alphabet] + 1
            else:
                maxlen = max(maxlen, index - start_index + 1)
            hashdict[alphabet] = index
        return maxlen


if __name__=="__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))