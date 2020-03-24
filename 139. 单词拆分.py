class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # 划分型DP
        wordDict = set(wordDict)
        if s in wordDict: return True
        f = [False] * (len(s)+1)  # 前n个字符串[0:n]能否被拆分
        f[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and f[j]:
                    f[i] = True
                    break
        return f[-1]


s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak(s, wordDict))
