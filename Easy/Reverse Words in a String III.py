class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([word[::-1] for word in s.split()])


# print(Solution().reverseWords(" teL's ekat edoCteeL tsetnoc "))