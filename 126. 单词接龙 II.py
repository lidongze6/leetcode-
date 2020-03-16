class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        from collections import defaultdict
        dic = set(wordList)
        dic.add(endWord)
        level = {beginWord}
        parents = defaultdict(set)
        while level and endWord not in parents:
            next_level = defaultdict(set)
            for word in level:
                for char in "abcdefghijklmnopqrstuvwxyz":
                    for i in range(len(beginWord)):
                        n = word[:i] + char + word[i + 1:]
                        if n in dic and n not in parents:
                            next_level[n].add(word)
            level = next_level
            parents.update(next_level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
print(s.findLadders(beginWord, endWord, wordList))
