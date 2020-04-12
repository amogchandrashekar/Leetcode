"""
HTML entity parser is the parser that takes HTML code as input and replace all the entities
of the special characters by the characters itself.

The special characters and their entities for HTML are:

Quotation Mark: the entity is &quot; and symbol character is ".
Single Quote Mark: the entity is &apos; and symbol character is '.
Ampersand: the entity is &amp; and symbol character is &.
Greater Than Sign: the entity is &gt; and symbol character is >.
Less Than Sign: the entity is &lt; and symbol character is <.
Slash: the entity is &frasl; and symbol character is /.
Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.

Example 1:

Input:
    text = "&amp; is an HTML entity but &ambassador; is not."
Output:
    "& is an HTML entity but &ambassador; is not."
Explanation:
    The parser will replace the &amp; entity by &
"""
import re


class Solution:
    def entityParser(self, text: str) -> str:
        text = re.sub(r"&quot;", '"', text)
        text = re.sub(r"&apos;", "'", text)
        text = re.sub(r"&amp;", "&", text)
        text = re.sub(r"&gt;", ">", text)
        text = re.sub(r"&lt;", "<", text)
        text = re.sub(r"&frasl;", "/", text)
        return text


if __name__ == "__main__":
    text = "leetcode.com&frasl;problemset&frasl;all"
    print(Solution().entityParser(text))