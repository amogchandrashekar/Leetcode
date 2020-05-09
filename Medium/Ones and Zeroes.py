"""
Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.



Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".


Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""


from typing import List
from collections import Counter


class Solution:
    def findMaxForm(self, strings: List[str], m: int, n: int) -> int:
        dp = [[[0 for i in range(n + 1)] for j in range(m + 1)] for k in range(len(strings) + 1)]
        for index in range(1, len(strings) + 1):
            counter = Counter(strings[index - 1])
            ones, zeroes = counter["1"], counter["0"]
            for row_index in range(m + 1):
                for col_index in range(n + 1):
                    if zeroes <= row_index and ones <= col_index:
                        dp[index][row_index][col_index] = max(dp[index - 1][row_index - zeroes][col_index - ones] + 1,
                                                              dp[index - 1][row_index][col_index])
                    else:
                        dp[index][row_index][col_index] = dp[index - 1][row_index][col_index]
        return dp[-1][-1][-1]


if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(Solution().findMaxForm(strs, m, n))