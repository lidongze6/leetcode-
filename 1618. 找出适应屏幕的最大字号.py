# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
# class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
#
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        l, r = 0, len(fonts) - 1
        while l < r:
            mid = l + (r - l) // 2 + 1
            sum_w = sum([fontInfo.getWidth(fonts[mid], char) for char in text])
            max_h = fontInfo.getHeight(fonts[mid])

            if sum_w <= w and max_h <= h:
                l = mid
            else:
                r = mid - 1

        sum_w = sum([fontInfo.getWidth(fonts[r], char) for char in text])
        max_h = fontInfo.getHeight(fonts[r])
        return fonts[r] if sum_w <= w and max_h <= h else -1
