class Solution:
    def findSubstringInWraproundString(self, p: str):
        l = len(p)
        if l <= 1:
            return l
        f = [0] * 26  # 以字母i为结尾的字串的个数
        f[ord(p[0]) - 97] = 1
        tmp = 1
        for i in range(1,len(p)):
            if (ord(p[i]) - ord(p[i - 1]) + 26) % 26 == 1:
                tmp += 1
            else:
                tmp = 1
            f[ord(p[i]) - 97] = max(f[ord(p[i]) - 97], tmp)
        return sum(f)
