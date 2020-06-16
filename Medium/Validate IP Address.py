"""
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers,
each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits.
The groups are separated by colons (":").
For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one.
Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones,
so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::)
to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid.
For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
"""

import re


class Solution:
    def validIPAddress(self, IP: str) -> str:
        ## RC ##
        ## APPROACH : REGEX ##

        ## TIME COMPLEXICITY : O(1) ##  (because the patterns to match have constant length.)
        ## SPACE COMPLEXICITY : O(1) ##

        # validating single IPv4 chunk using Regular Expression
        def validate_IPv4_regex(chunks):
            return re.match(r'(' + IPv4_chunk_pattern + ')', chunk)

        # validating single IPv6 chunk using Regular Expression
        def validate_IPv6_regex(chunk):
            return re.match(r'(' + IPv6_chunk_pattern + ')', chunk)

        # ^ -> start, $ -> end. They are necessary else if any substring matched also it returns true
        IPv4_chunk_pattern = "^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"  # indicates 0-9 or 10-99 or 100-199 or 200-49 or 250-255.
        IPv6_chunk_pattern = "^([0-9a-fA-F]{1,4})$"  # 0-9|a-f|A-F of length 1 to 4.

        if IP.count('.') == 3:
            for chunk in IP.split("."):
                if not validate_IPv4_regex(chunk):
                    return "Neither"
            return "IPv4"
        elif IP.count(':') == 7:
            for chunk in IP.split(":"):
                if not validate_IPv6_regex(chunk):
                    return "Neither"
            return "IPv6"
        return "Neither"