"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_bracket, right_bracket, remove = list(), list(), list()
        new_str = ""
        for index, letter in enumerate(s):
            if letter == "(":
                left_bracket.append(index)
            elif letter == ")":
                if left_bracket:
                    left_bracket.pop()
                else:
                    remove.append(index)

        remove = set(remove + left_bracket)
        for index, letter in enumerate(s):
            if index not in remove:
                new_str += letter
        return new_str


if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    print(Solution().minRemoveToMakeValid(s))