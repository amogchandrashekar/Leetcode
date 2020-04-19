"""
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by
another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b"
are also valid permutations
"""


class Solution:
    def reformat(self, s: str) -> str:
        alpha, num = list(), list()
        for letter in s:
            if letter.isalpha():
                alpha.append(letter)
            else:
                num.append(letter)

        if abs(len(alpha) - len(num)) <= 1:
            if len(alpha) > len(num):
                return alpha[0] + "".join(a + d for a, d in zip(num, alpha[1:]))
            elif len(num) > len(alpha):
                return num[0] + "".join(a + d for a, d in zip(alpha, num[1:]))
            else:
                return "".join(a + d for a, d in zip(alpha, num))
        else:
            return ""


if __name__=="__main__":
    print(Solution().reformat("couv2019"))