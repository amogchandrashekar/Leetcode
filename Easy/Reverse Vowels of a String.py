"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = "AEIOUaeiou"
        vowels = set(vowels)
        s = list(s)
        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowels:
                left += 1
            else:
                right -= 1
        return "".join(s)


if __name__ == "__main__":
    s = 'leetcode'
    print(Solution().reverseVowels(s))