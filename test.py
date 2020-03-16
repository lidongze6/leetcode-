class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        from collections import defaultdict
        dic = set(wordList)
        level = {beginWord: [beginWord]}
        parent = defaultdict(list)
        while level:
            next_level = defaultdict(list)
            for word in level:
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + j + word[i + 1:]
                        if new_word in dic:
                            next_level[new_word] = [j + [new_word] for j in level[word]]
            dic -= next_level.keys()
            level = next_level

        return parent


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
print(s.findLadders(beginWord, endWord, wordList))
