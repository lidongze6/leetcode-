class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        from collections import defaultdict
        wordlist = set(wordList)
        res = []
        level = {}
        level[beginWord] = [[beginWord]]

        while level:
            next_level = defaultdict(list)
            for word in level:
                if word == endWord:
                    res.extend(k for k in level[word])
                else:
                    for i in range(len(word)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            newword = word[:i] + c + word[i + 1:]
                            if newword in wordlist:
                                next_level[newword] += [j + [newword] for j in level[word]]
            wordlist -= set(next_level.keys())
            level = next_level

        return res


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
print(s.findLadders(beginWord, endWord, wordList))