from functools import lru_cache
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid_parantheses(text_str):
            open_parantheses = 0
            imbalance = 0

            for char in text_str:
                if char.isalpha():
                    continue

                if char == '(':
                    open_parantheses += 1
                elif char == ')':
                    if open_parantheses > 0:
                        open_parantheses -= 1
                    else:
                        imbalance += 1

            return imbalance + open_parantheses

        res = set()

        @lru_cache(maxsize=None)
        def dfs(text_str, removals):

            nonlocal res
            if removals == 0 and is_valid_parantheses(text_str) == 0:
                res.add(text_str)
                return

            for ind in range(len(text_str)):
                if text_str[ind].isalpha():
                    continue
                dfs(text_str[: ind] + text_str[ind + 1:], removals - 1)

        min_removals = is_valid_parantheses(s)
        dfs(s, min_removals)
        return list(res)