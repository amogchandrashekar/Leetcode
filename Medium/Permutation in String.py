"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_substring, counter_string = defaultdict(int), defaultdict(int)
        for x in s1: counter_substring[x] += 1
        for x in s2[: len(s1)]: counter_string[x] += 1
        start, end = 0, len(s1)
        while end < len(s2):
            if counter_string == counter_substring:
                return True
            counter_string[s2[start]] -= 1
            if counter_string[s2[start]] <= 0:
                counter_string.pop(s2[start])
            counter_string[s2[end]] += 1
            start += 1
            end += 1
        return counter_string == counter_substring


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))