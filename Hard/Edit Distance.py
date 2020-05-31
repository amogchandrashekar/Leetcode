"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        rows, cols = len(dp), len(dp[0])
        for i in range(cols):
            dp[0][i] = i
        for i in range(rows):
            dp[i][0] = i

        for row_index in range(1, len(dp)):
            for col_index in range(1, len(dp[row_index])):
                if word2[row_index - 1] == word1[col_index - 1]:
                    dp[row_index][col_index] = dp[row_index - 1][col_index - 1]
                else:
                    dp[row_index][col_index] = min(dp[row_index][col_index - 1], dp[row_index - 1][col_index],
                                                   dp[row_index - 1][col_index - 1]) + 1

        return dp[-1][-1]


if __name__ == "__main__":
    word1 = "intention"
    word2 = "execution"
    print(Solution().minDistance(word1, word2))
