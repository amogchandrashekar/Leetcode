from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ans = ""
        for x in words:
            ans += x
            if ans == s:
                return True
            if len(ans) > len(s):
                return False
        return False