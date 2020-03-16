class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def revers(s, l, r):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            revers(s, l + 1, r - 1)

        l = 0
        r = len(s) - 1
        revers(s, l, r)


r = Solution()
s = ["h", "e", "l", "l", "o"]
r.reverseString(s)
print(s)
