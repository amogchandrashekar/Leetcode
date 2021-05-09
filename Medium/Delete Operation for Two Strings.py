"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word1) + 1) for _ in range(len(word2) + 1)]

        for i in range(len(word2) + 1):
            dp[i][len(word1)] = len(word2) - i
        for j in range(len(word1) + 1):
            dp[len(word2)][j] = len(word1) - j

        for rid in range(len(word2) - 1, -1, -1):
            for cid in range(len(word1) - 1, -1, -1):
                dp[rid][cid] = min(dp[rid][cid + 1], dp[rid + 1][cid]) + 1 if word2[rid] != word1[cid] else \
                    dp[rid + 1][cid + 1]

        return dp[0][0]


if __name__ == '__main__':
    word1 = 'amog'
    word2 = 'pushpa'
    print(Solution().minDistance(word1, word2))