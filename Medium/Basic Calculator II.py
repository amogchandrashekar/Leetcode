class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = list()
        prev_symbol = '+'  # to add first number always

        for i in range(len(s)):

            if s[i].isnumeric():
                num = (num * 10) + int(s[i])

            if s[i] in '+*/-' or i == len(s) - 1:
                if prev_symbol == '+':
                    stack.append(num)

                elif prev_symbol == '-':
                    stack.append(-num)

                elif prev_symbol == '*':
                    stack.append(stack.pop() * num)

                elif prev_symbol == '/':
                    stack.append(int(stack.pop() / num))

                num = 0
                prev_symbol = s[i]

        return sum(stack)


if __name__ == '__main__':
    s = "14-3/2"
    print(Solution().calculate(s))