class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = 0
        res = ""
        while l + 2 * k <= len(s):
            res = res + s[l:l + k][::-1] + s[l + k:l + 2 * k]
            l += 2 * k
        res += s[l:l + k][::-1] + s[l + k:] if len(s) - l + 1 >= k else s[l:][::-1]
        return res
