"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.



Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1


Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
"""
import itertools


class Solution:
    def maxPower_one_liner(self, s: str) -> int:
        return max(len(list(b)) for a, b in itertools.groupby(s))

    def maxPower(self, s: str) -> int:
        prev, counter, best = None, 0, 0
        for char in s:
            if char == prev:
                counter += 1
                best = max(best, counter)
            else:
                counter = 1
                prev = char
        return best


if __name__ == "__main__":
    s = "leetcode"
    print(Solution().maxPower(s))