class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = len(text.split())
        spaces = 0
        for char in text:
            if char == ' ':
                spaces += 1

        if words > 1:
            spacing = spaces // (words - 1)
            remaining = spaces % (words - 1)
        else:
            spacing = 0
            remaining = spaces

        answer = (" " * spacing).join(text.split())
        return answer + (" " * remaining)