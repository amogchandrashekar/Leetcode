"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = list()
        counter_string, counter_pattern = Counter(s[:len(p)]), Counter(p)
        start, end = 0, len(p)
        while end <= len(s):
            if counter_string == counter_pattern:
                anagrams.append(start)
            counter_string[s[start]] -= 1
            if counter_string[s[start]] <= 0:
                counter_string.pop(s[start])
            if end < len(s):
                counter_string[s[end]] += 1
            start += 1
            end += 1
        return anagrams


if __name__ == "__main__":
    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s, p))
