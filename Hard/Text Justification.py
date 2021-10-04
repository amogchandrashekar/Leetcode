from typing import List
from collections import defaultdict


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Time complexity: O(m*n)
        Space complexity: O(m*n)
        :param words:
        :param maxWidth:
        :return:
        """
        line = list()
        cur_line_width = 0
        answer = list()

        def justify(line, cur_line_width):
            all_possible_spaces = maxWidth - cur_line_width
            number_of_positions_of_spaces = len(line) - 1

            if number_of_positions_of_spaces == 0:
                return line[0] + " " * all_possible_spaces

            equally_divided_spaces = all_possible_spaces // number_of_positions_of_spaces
            remaining_extra_spaces = all_possible_spaces % number_of_positions_of_spaces
            position_of_spaces = [equally_divided_spaces] * number_of_positions_of_spaces
            for ind in range(remaining_extra_spaces):
                position_of_spaces[ind] += 1

            sentence = ''
            for ind, word in enumerate(line):
                sentence += word
                if ind < len(position_of_spaces):
                    sentence += " " * position_of_spaces[ind]

            return sentence

        for word in words:
            if len(word) + len(line) + cur_line_width <= maxWidth:
                line.append(word)
                cur_line_width += len(word)

            else:
                answer.append(justify(line, cur_line_width))
                line = [word]
                cur_line_width = len(word)

        last_line = " ".join(line)
        remaining_spaces = maxWidth - len(last_line)
        answer.append(last_line + " " * remaining_spaces)

        return answer


if __name__ == '__main__':
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    print(Solution().fullJustify(words, maxWidth))
