class Solution:
    def stacky(self, s):
        stack = []

        for char in s:

            if char != ']':
                stack.append(char)

            else:
                decoded_text = ''
                number = ''

                while stack and stack[-1].isalpha():
                    decoded_text = stack.pop() + decoded_text

                stack.pop()

                while stack and stack[-1].isnumeric():
                    number = stack.pop() + number

                stack.append(decoded_text * int(number))

        return "".join(stack)


if __name__ == '__main__':
    s = "3[a2[c]]"
    print(Solution().stacky(s))
