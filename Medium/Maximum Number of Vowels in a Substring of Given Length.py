"""
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
Example 5:

Input: s = "tryhard", k = 4
Output: 1


Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length
"""

from collections import defaultdict


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ("a", "e", "i", "o", "u")
        counter = defaultdict(int)

        max_ln = 0
        for letter in s[:k]:
            if letter in vowels:
                counter[letter] += 1
                max_ln += 1
        start, end = 0, k

        ans = 0

        while end <= len(s):
            ans = max(ans, max_ln)
            if max_ln == k:
                return max_ln
            if end < len(s) and s[end] in vowels:
                counter[s[end]] += 1
                max_ln += 1
            if s[start] in vowels:
                counter[s[start]] -= 1
                max_ln -= 1
                if counter[s[start]] <= 0:
                    counter.pop(s[start])
            end += 1
            start += 1
        return ans


if __name__ == "__main__":
    s = "weallloveyou"
    k = 7
    print(Solution().maxVowels(s, k))