from typing import List


class Solution:
    def addBoldTag(self, string_txt: str, words: List[str]) -> str:
        bold = [False] * len(string_txt)

        for word in words:
            start = string_txt.find(word)
            while start != -1:
                for ind in range(start, start + len(word)):
                    bold[ind] = True
                start = string_txt.find(word, start + 1)

        res = ''
        ind = 0

        while ind < len(string_txt):

            if not bold[ind]:
                res += string_txt[ind]
                ind += 1

            else:
                res += '<b>'
                while ind < len(string_txt) and bold[ind]:
                    res += string_txt[ind]
                    ind += 1
                res += '</b>'

        return res


if __name__ == '__main__':
    s = "aaabbcc"
    words = ["aaa", "aab", "bc"]
    print(Solution().addBoldTag(s, words))
