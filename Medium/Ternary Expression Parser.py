"""
Given a string representing arbitrarily nested ternary expressions,
calculate the result of the expression.
You can always assume that the given expression is valid and only consists of digits 0-9, ?, :,
T and F (T and F represent True and False respectively).

The length of the given string is ≤ 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.
"""


class Solution:
    """
    @param expression: a string, denote the ternary expression
    @return: a string
    """

    def parseTernary(self, expression: str) -> str:

        stack = []
        i = len(expression) - 1
        while i >= 1:
            if expression[i] == '?':
                left, right = stack.pop(), stack.pop()
                stack.append(left if expression[i - 1] == 'T' else right)
                i -= 1
            elif expression[i] != ':':
                stack.append(expression[i])
            i -= 1
        return stack[0]


if __name__ == '__main__':
    exp = "F?1:T?3:1"
    print(Solution().parseTernary(exp))