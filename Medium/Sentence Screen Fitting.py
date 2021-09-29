class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        curr_word_idx = 0
        total_complete_sentence = 0
        complete_sentence = '-'.join(sentence)
        memo = dict()

        for row in range(rows):

            if curr_word_idx in memo:
                complete_sentence_in_row, next_word_idx = memo[curr_word_idx]
                total_complete_sentence += complete_sentence_in_row
                curr_word_idx = next_word_idx

            else:
                old_word_idx = curr_word_idx
                complete_sentence_in_row = 0
                cur_column = 0

                while cur_column < cols:
                    curr_word_len = len(sentence[curr_word_idx])

                    # break if the new word is not possible to be accomodated
                    if cols - cur_column < curr_word_len:
                        break

                    cur_column += curr_word_len + 1  # 1 owing to -

                    # indicating completion of the words of the sentence
                    if curr_word_idx == len(sentence) - 1:
                        complete_sentence_in_row += 1
                        if cur_column + len(complete_sentence) < cols:
                            accomodatable_complete_sentence = (cols - cur_column) // (len(complete_sentence) + 1)
                            complete_sentence_in_row += accomodatable_complete_sentence
                            cur_column += (len(complete_sentence) + 1) * (accomodatable_complete_sentence)

                    curr_word_idx = (curr_word_idx + 1) % len(sentence)  # rollback

                total_complete_sentence += complete_sentence_in_row
                memo[old_word_idx] = [complete_sentence_in_row, curr_word_idx]

        return total_complete_sentence


if __name__ == '__main__':
    rows = 3
    cols = 25
    sentence = ["a", "bcd", "e"]
    print(Solution().wordsTyping(sentence, rows, cols))