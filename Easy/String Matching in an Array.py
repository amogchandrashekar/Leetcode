"""
Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or
right side of words[j].

Example 1:
Input:
    words = ["mass","as","hero","superhero"]
Output:
    ["as","hero"]
Explanation:
    "as" is substring of "mass" and "hero" is substring of "superhero".
    ["hero","as"] is also a valid answer.

Example 2:
Input:
    words = ["leetcode","et","code"]
Output:
    ["et","code"]
Explanation:
    "et", "code" are substring of "leetcode".

Example 3:
Input:
    words = ["blue","green","bu"]
Output:
    []
"""

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        answer = set()
        for index, word in enumerate(words):
            for j, comp_word in enumerate(words[index+1:]):
                if word in comp_word:
                    answer.add(word)
        return list(answer)


if __name__=="__main__":
    print(Solution().stringMatching(["leetcoder","leetcode","od","hamlet","am"]))