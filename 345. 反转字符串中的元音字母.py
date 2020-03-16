class Solution:
    def reverseVowels(self, s):
        st = "aeiouAEIOU"
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l] not in st:
                l += 1
            while l < r and s[r] not in st:
                r -= 1
            if s[l] in st and s[r] in st:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)


s = "hello"
print(Solution().reverseVowels(s))
