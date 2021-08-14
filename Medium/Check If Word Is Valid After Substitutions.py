class Solution:
    def isValid(self, s: str) -> bool:

        while s:
            prev = s
            s = s.replace('abc', '')
            if prev == s:
                return False

        return True

    def is_valid_stacks(self, s):
        stack = list()

        for char in s:
            stack.append(char)

            if len(stack) >= 3 and stack[-1] == 'c' and stack[-2] == 'b' and stack[-3] == 'a':
                stack.pop()
                stack.pop()
                stack.pop()

        return len(stack) == 0

