class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        dic = {"0": 0, "1": 0}
        res = 0
        tmp = 0
        for i in range(len(s)):
            if i == 0:
                dic[s[i]] += 1
            if i > 0 and s[i - 1] == s[i]:
                dic[s[i]] += 1
            elif i > 0 and s[i - 1] != s[i]:
                res += min(tmp, dic[s[i - 1]])
                tmp, dic[s[i - 1]] = dic[s[i - 1]], 0
                dic[s[i]] = 1
        return res + min(tmp, dic[s[-1]])
