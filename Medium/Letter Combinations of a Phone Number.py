"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [] # If no digits are there, return empty list
        hash_map = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
                    }
        answer = list()

        def dfs(text_str, index=0):
            if len(text_str) == len(digits):
                answer.append(text_str) # Bound condition to stop recursion and return
                return

            while index < len(digits):
                number = digits[index]
                for letter in hash_map[number]:
                    dfs(text_str + letter, index + 1) # recursively use breadth first search to construct the string
                return

        dfs("")
        return answer


if __name__ == "__main__":
    numbers = ""
    print(Solution().letterCombinations(numbers))

