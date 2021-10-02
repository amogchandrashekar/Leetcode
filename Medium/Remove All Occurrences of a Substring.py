class Solution:
    def removeOccurrences(self, text_str: str, pattern: str) -> str:
        pi_table = [0]
        pi_ind = 0

        for pattern_ind in range(1, len(pattern)):

            while pi_ind and pattern[pattern_ind] != pattern[pi_ind]:
                pi_ind = pi_table[pi_ind - 1]

            if pattern[pattern_ind] == pattern[pi_ind]:
                pi_ind += 1

            pi_table.append(pi_ind)

        stack = [["", 0]]
        pattern_ind = 0

        for char in text_str:
            stack.append([char, pattern_ind])

            while pattern_ind and pattern[pattern_ind] != char:
                pattern_ind = pi_table[pattern_ind - 1]

            if pattern[pattern_ind] == char:
                pattern_ind += 1

            if pattern_ind == len(pattern):
                for _ in range(len(pattern)):
                    _, pattern_ind = stack.pop()

        return "".join(char for char, _ in stack)


if __name__ == '__main__':
    s = "daabcbaabcbc"
    part = "abc"
    print(Solution().removeOccurrences(s, part))
