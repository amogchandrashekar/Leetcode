class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack = list()

        for node in preorder:
            stack.append(node)

            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#":
                stack.pop()
                stack.pop()
                if stack[-1] == "#":
                    return False
                stack.pop()
                stack.append("#")

        return stack == ['#']