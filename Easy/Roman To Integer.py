# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:
    def romanToInt(self, symbols):
        reference_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = reference_dict[symbols[0]]
        previous = reference_dict[symbols[0]]
        for symbol in symbols[1:]:
            current = reference_dict[symbol]
            value += current
            if current > previous:
                value -= 2*previous
            previous = current
        return (value)


if __name__ == "__main__":
    print(Solution().romanToInt("IV"))