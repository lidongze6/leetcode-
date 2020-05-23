class Solution:
    def maxProduct(self, words) -> int:
        li = [0] * len(words)
        for i in range(len(words)):
            for s in words[i]:
                li[i] |= 1 << (ord(s) - 97)

        res = 0
        for i in range(1, len(words)):
            for j in range(i):
                if li[i] & li[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res


words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(Solution().maxProduct(words))
