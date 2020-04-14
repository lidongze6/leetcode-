class Solution:
    def longestStrChain(self, words) -> int:
        l = len(words)
        words.sort(key=len)
        if l <= 1: return l
        dic = dict()
        res=0
        for w in words:
            if w not in dic:
                dic[w] = 1
            for k in range(len(w)):
                tmp = w[:k] + w[k + 1:]
                if tmp in dic:
                    dic[w] = max(dic[w], dic[tmp]+1)
            res=max(res,dic[w])
        return res
