class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        rptr, wptr = 0, 0
        while rptr < len(chars):
            ch, f = chars[rptr], 0
            while rptr < len(chars) and chars[rptr] == ch:
                rptr, f = rptr+1, f+1
            chars[wptr], wptr = ch, wptr + 1
            if f > 1:
                for c in str(f):
                    chars[wptr], wptr = c, wptr + 1
        return wptr


if __name__ == '__main__':
    chars = ["a","a","b","b","c","c","c"]
    print(Solution().compress(chars))