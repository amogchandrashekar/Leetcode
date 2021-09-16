from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block_comment_open = False
        buffer = ''
        ans = []

        for source_line in source:

            ind = 0

            while ind < len(source_line):
                char = source_line[ind]

                # handle //
                if char == '/' and ind + 1 < len(source_line) and source_line[ind + 1] == '/' and not block_comment_open:
                    ind = len(source_line)

                # handle /*
                elif char == '/' and not block_comment_open and ind + 1 < len(source_line) and source_line[ind + 1] == '*':
                    block_comment_open = True
                    ind += 1

                # handle */
                elif char == '*' and block_comment_open and ind + 1 < len(source_line) and source_line[ind + 1] == '/':
                    block_comment_open = False
                    ind += 1

                elif not block_comment_open:
                    buffer += char

                ind += 1

            if buffer and not block_comment_open:
                ans.append(buffer)
                buffer = ''

        return ans


if __name__ == '__main__':
    source = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]
    print(Solution().removeComments(source))