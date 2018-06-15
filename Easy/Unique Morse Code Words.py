

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformations = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                           "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        unique_words = set()

        # 97 is where the lowercase numbers start.
        #ord() function in Python. Given a string of length one, return an integer representing the Unicode code point of the character
        #ord('a')=97

        for word in words:
            transformation = ""
            for letter in word:
                transformation += transformations[(ord(letter) - 97)]
            unique_words.add(transformation)
            #as unique_words is a set, it does not add the duplicate entries


# print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))