"""
Given an array of strings, group anagrams together.

Example:

Input:
    ["eat", "tea", "tan", "ate", "nat", "bat"],

Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for ana in strs:
            answer[tuple(sorted(ana))].append(ana)
        return answer.values()


if __name__=="__main__":
    user_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(user_input))