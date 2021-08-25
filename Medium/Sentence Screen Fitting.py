class Solution:
    """
    @param sentence: a list of string
    @param rows: an integer
    @param cols: an integer
    @return: return an integer, denote times the given sentence can be fitted on the screen
    """
    def wordsTyping(self, sentence, rows, cols):
        # Write your code here
        complete_sentence = '-'.join(sentence)
        ans = 0
        remaining = complete_sentence

        if len(remaining) == cols:
            return rows

        for row in range(rows):
            while len(remaining) <= cols:
                remaining += "-" + complete_sentence
                ans += 1

            cut_index = cols
            while remaining[cut_index] != '-':
                cut_index -= 1

            remaining = remaining[cut_index:].strip('-')

        return ans


if __name__ == '__main__':
    rows = 868
    cols = 942
    sentence = ["bcgqp", "xlqayc", "jzsxzhu", "ycxbxpxllq", "xqhz", "xtkegmw", "rtmye", "sxszyk", "mogkdakn", "tul", "jfn", "wh", "lldk", "schxgncgw", "jfdosso", "vnmxlag", "vkfo", "pzn", "nvyhr", "cqkerpihgn", "rrlggse"]
    print(Solution().wordsTyping(sentence, rows, cols))