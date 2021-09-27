class Solution:
    def lengthLongestPath(self, input: str) -> int:
        directories = input.split('\n')
        stack = list()  # [\t len, total_len]
        ans = 0

        for sub_dir in directories:

            number_of_tabs = sub_dir.count('\t')
            while stack and stack[-1][0] >= number_of_tabs:
                stack.pop()
            old_dir_len = stack[-1][-1] if stack else 0
            cur_dir_lin = len(sub_dir.strip('\t'))

            if '.' in sub_dir:
                ans = max(ans, old_dir_len + cur_dir_lin)
            else:
                stack.append([number_of_tabs, old_dir_len + cur_dir_lin + 1])

        return ans


if __name__ == '__main__':
    p = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(Solution().lengthLongestPath(p))