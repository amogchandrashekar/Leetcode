from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()

        left, right = 0, len(products) - 1
        for ind, char in enumerate(searchWord):
            while left < right and (len(products[left]) <= ind or products[left][ind] != char):
                left += 1

            while left < right and (len(products[right]) <= ind or products[right][ind] != char):
                right -= 1

            ans.append(products[left: min(right + 1, left + 3)])

        return ans


if __name__ == '__main__':
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(Solution().suggestedProducts(products, searchWord))