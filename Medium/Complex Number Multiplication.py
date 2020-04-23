"""
Given two strings representing two complex numbers.
You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:
The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the
range of [-100, 100]. And the output should be also in this form.
"""

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a = a.split("+")
        b = b.split("+")
        real_a, complex_a = int(a[0]), int(a[1][:-1])
        real_b, complex_b = int(b[0]), int(b[1][:-1])
        res_real = (real_a * real_b) - (complex_a * complex_b)
        res_comp = (real_a * complex_b) + (real_b * complex_a)
        return str(res_real) + "+" + str(res_comp) + "i"


if __name__ == "__main__":
    a = "0+0i"
    b = "0+0i"
    print(Solution().complexNumberMultiply(a, b))