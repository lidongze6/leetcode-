class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 本题关键是找到当前滑动窗口中出现最多字母的个数，用窗口大小减去这个个数，得到的即为剩下要替换的
        # 字母的个数，若这个个数大于k，则窗口缩小，若小于k，则窗口扩大
        dic = dict()
        l, r = 0, 0
        res = 0
        while r < len(s):
            dic[s[r]] = dic.get(s[r], 0) + 1
            max_letter = max(dic, key=dic.get)
            while r - l + 1 - dic[max_letter] > k:
                dic[s[l]] -= 1
                l += 1
                max_letter = max(dic, key=dic.get)
            res = max(res, r - l + 1)
            r += 1
        return res


s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))
