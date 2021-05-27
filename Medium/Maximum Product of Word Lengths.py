class Solution(object):
    def sign(self, word):
        value = 0
        for c in word:
            value = value | (1 << (ord(c)-97))
        return value

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        signature = [self.sign(x) for x in words]
        max_product, N = 0, len(words)
        for i in range(N):
            for j in range(i+1, N):
                if signature[i] & signature[j] == 0:
                    max_product = max(max_product, len(words[i])*len(words[j]))
        return max_product


if __name__ == '__main__':
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    print(Solution().maxProduct(words))